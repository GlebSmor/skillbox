from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Product, Order
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductsListView(ListView):
    template_name = "shop/products-list.html"
    queryset = Product.objects.all()
    context_object_name = "products"
    
    
class ProductDetailView(DetailView):
    template_name = "shop/product-detail.html"
    model = Product
    context_object_name = "product"
    
    
class OrderDetailView(DetailView):
    template_name = "shop/order-detail.html"
    context_object_name = "order"
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )
    
    
class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    fields = "user", "products", "delivery_address", "promocode"
    success_url = reverse_lazy("auth:account")
    
    # def get_success_url(self):
    #     products_in_order = self.request.POST.getlist("products")
        
    #     products = []
    #     for i in products_in_order:
    #         products.append(Product.objects.filter(id=i).only("price"))
            
    #     prices = []
    #     for i in products:
    #         prices.append(i.values("price")[0]["price"])
            
            

    #     return reverse_lazy("auth:account")