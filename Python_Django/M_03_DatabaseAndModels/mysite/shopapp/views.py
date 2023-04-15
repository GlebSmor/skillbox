from django.shortcuts import render
from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponse
from timeit import default_timer
from .models import Product, Order

def shop_index(request: HttpRequest):
    products = [
        ('laptop', 1999),
        ('desktop', 3999),
        ('smartphone', 999),
    ]
    context = {
        'time_running': default_timer(),
        'products': products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)

def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.all(),
    }
    return render(request, 'shopapp/groups.html', context=context)

def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all()
    }
    return render(request, 'shopapp/products.html', context=context)

def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp/orders.html', context=context)