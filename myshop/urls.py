from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('cuentas/', include('cuentas.urls', namespace='cuentas')),
    path('social-auth/',include('social_django.urls', namespace='social')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('', include('shop.urls', namespace='shop')),
]#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#ya no necesitamos esto en produccion para servir los archivos ya que lo hacemos con Nginx 
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)