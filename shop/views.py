from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product,favoritos
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from .recommender import Recommender
from orders.models import Order
from django.core.paginator import Paginator


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(disponible=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')
    color = request.GET.get('color')
    talla = request.GET.get('talla')

    if precio_min and precio_max:
        products = products.filter(price__gte=precio_min, price__lte=precio_max)
    
    if color:
        products = products.filter(color=color)
    
    if talla:
        products = products.filter(talla=talla)

    paginator = Paginator(products, 2)  # 10 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'categories': categories,
        # 'products': products,
        'products': page_obj,
    }
    return render(request, 'shop/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,disponible=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request,'shop/detail.html',{'product': product,'cart_product_form': cart_product_form,'recommended_products': recommended_products})


@login_required
def favoritosview(request,pk):
    #if request.user.is_authenticated:
    producto = get_object_or_404(Product,pk=pk)
    favorito = favoritos.objects.filter(user=request.user,producto=producto)
    if favorito.exists():#si el usuario ya le dio favorito eliminalo
        favorito[0].delete()
        return redirect('shop:product_list')
    favoritos.objects.create(user=request.user,producto=producto)
    return redirect('shop:product_list')
    #return redirect('cuentas:login')