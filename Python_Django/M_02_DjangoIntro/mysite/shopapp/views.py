from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from timeit import default_timer


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
