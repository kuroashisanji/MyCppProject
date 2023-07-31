from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import Product
from django.db.models import Q

def index(request):
    products = Product.objects.all()

    cart = request.session.get('cart', {})
    cart_length = sum(cart.values())

    params = {'products': products, 'cart_length': cart_length}

    return render(request, "MyShopApp/index.html", params)

def search_results(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(product_name__icontains=query) | Q(desc__icontains=query)
        )
    else:
        products = Product.objects.none()

    cart = request.session.get('cart', {})
    cart_length = sum(cart.values())

    params = {'products': products, 'cart_length': cart_length, 'query': query}
    return render(request, "MyShopApp/search_results.html", params)


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, "MyShopApp/prodView.html", {'product': product[0]})


def checkoutView(request):
    return render(request, "MyShopApp/checkout.html")


def acknowledgementView(request):
    return render(request, "MyShopApp/acknowledgement.html")
