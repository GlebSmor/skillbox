from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


from .models import Product, Order


class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
        }
        return render(request, 'shopapp/shop-index.html', context=context)


class ProductDetailsView(DetailView):
    template_name = "shopapp/products-details.html"
    model = Product
    context_object_name = "product"


class ProductsListView(ListView):
    template_name = "shopapp/products-list.html"
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)


class ProductCreateView( CreateView):
    # def test_func(self):
    #     return self.request.user.has_perm("shopapp.add_product")
    model = Product
    fields = "name", "price", "description", "discount"
    success_url = reverse_lazy("shopapp:products_list")
    
    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)

class ProductUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        # if self.request.user.is_superuser: 
        #     return True
        if self.request.user.has_perm("shopapp.change_product") and self.get_object().created_by == self.request.user:
            return True
        else:
            return False
        
    model = Product
    fields = "name", "price", "description", "discount"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            "shopapp:product_details",
            kwargs={"pk": self.object.pk},
        )


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrdersListView(LoginRequiredMixin, ListView):
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )


class OrderDetailView(DetailView):
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )


class CreateOrderView(CreateView):
    model = Order
    fields = "user", "products", "delivery_address", "promocode"
    success_url = reverse_lazy("shopapp:order_list")
    

class UpdateOrderView(UpdateView):
    model = Order
    fields = "user", "products", "delivery_address", "promocode"
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse("shopapp:order_detail", kwargs={"pk": self.object.pk},)


class ProductsExportView(View):
    def get(self, request: HttpRequest):
        products = Product.objects.order_by("pk").all()
        products_data = [
            {
                "pk": pr.pk,
                "name": pr.name,
                "price": str(pr.price),
                "archived": pr.archived,
            }
            for pr in products
        ]
        return JsonResponse({"products": products_data})
    
    
class OrderExportView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff
    
    def get(self, request: HttpRequest):
        orders = Order.objects.order_by("pk").all()
        response = {"orders": [
            {
            "pk": order.pk,
            "delivery_address": order.delivery_address,
            "promocode": order.promocode,
            "user": order.user.pk,
            "products": [product.pk for product in order.products.all()]    
            }
            for order in orders
        ]
        }
        
        return JsonResponse(response)