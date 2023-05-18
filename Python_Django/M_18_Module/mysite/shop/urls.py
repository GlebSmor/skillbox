from django.urls import path, include

from .views import ProductDetailView, ProductsListView, OrderDetailView, CreateOrderView
from bonuses.views import home


app_name = "shop"


urlpatterns = [
    path('', home, name='home'),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("orders/create/", CreateOrderView.as_view(), name="order_create"),
    
]