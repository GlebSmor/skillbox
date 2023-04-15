from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponse
from timeit import default_timer
from .models import Product, Order
from .forms import ProductForm, OrderForm


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

def create_product(request: HttpRequest):
    if request.method =="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            url = resolve_url("shopapp:products_list")
            return redirect(url)
        
    else:   
        form = ProductForm()
    context = {
        "form": form,
    }
    
    return render(request, 'shopapp/create-product.html', context=context)

def create_order(request: HttpRequest):
    if request.method =="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            url = resolve_url("shopapp:orders_list")
            return redirect(url)
    else:
        form = OrderForm()
    context = {
        "form": form,
    }
    
    return render(request, 'shopapp/create-order.html', context=context)