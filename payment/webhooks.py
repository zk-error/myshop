import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order
from .tasks import payment_completed
from shop.recommender import Recommender

recommender = Recommender()


@csrf_exempt #decorador evitar que Django realice la validación CSRF
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None 

    try:
        event = stripe.Webhook.construct_event(payload,sig_header,settings.STRIPE_WEBHOOK_SECRET)
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event.type == 'checkout.session.completed':
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                order = Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
            order.paid = True
            order.stripe_id = session.payment_intent
            order.save()
            payment_completed.delay(order.id)
            products = order.items.values_list('product_id', flat=True)
            recommender.products_bought(products)
    #se ejecutará si no se ha producido ninguna excepción en el código anterior y si no se han encontrado errores 
    return HttpResponse(status=200)


