from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.models import Group
from django.http import HttpRequest, HttpResponseRedirect
from timeit import default_timer
from django.urls import reverse_lazy, reverse

from django.views import View
from django.views.generic import (DetailView, ListView, CreateView, 
                                  UpdateView, DeleteView)
from .models import Product, Order
from .forms import ProductForm, OrderForm, GroupForm


class ShopIndexView(View):
    def get(self, request: HttpRequest):
        products = [
            ("laptop", 1999),
            ("desktop", 3999),
            ("smartphone", 999),
        ]
        context = {
            "time_running": default_timer(),
            "products": products,
        }
        return render(request, "shopapp/shop-index.html", context=context)


class GroupsListView(View):
    def get(self, request: HttpRequest):
        context = {
            "form": GroupForm(),
            "groups": Group.objects.all(),
        }
        return render(request, "shopapp/groups.html", context=context)
    
    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.path)


class ProductDetailsView(DetailView):
    template_name = "shopapp/product-details.html"
    # model = Product
    context_object_name = "product"
    queryset = Product.objects.filter(archived=False)
 
    
class ProductsListView(ListView):
    template_name = "shopapp/products.html"
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)
    

class CreateProductView(CreateView):
    model = Product
    fields = "name", "price", "description", "discount"
    success_url = reverse_lazy("shopapp:products_list")
    

class UpdateProductView(UpdateView):
    model = Product
    fields = "name", "price", "description", "discount"
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse("shopapp:products_details", kwargs={"pk": self.object.pk},)


class DeleteProductView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")
    
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save(update_fields=['archived'])
        return HttpResponseRedirect(success_url)


class OrdersListView(ListView):
    queryset = Order.objects.select_related("user").prefetch_related("products")


class OrdersDetailsView(DetailView):
    queryset = Order.objects.select_related("user").prefetch_related("products")
    
    
class CreateOrderView(CreateView):
    model = Order
    fields = "user", "products", "dilivery_adress", "promocode"
    success_url = reverse_lazy("shopapp:orders_list")
    

class UpdateOrderView(UpdateView):
    model = Order
    fields = "user", "products", "dilivery_adress", "promocode"
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse("shopapp:order_details", kwargs={"pk": self.object.pk},)


class DeleteOrderView(DeleteView):
    model = Order
    success_url = reverse_lazy("shopapp:orders_list")
