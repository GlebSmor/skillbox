from django.urls import path
from .views import (ShopIndexView, GroupsListView, 
                    ProductDetailsView, ProductsListView,
                    OrdersListView, OrdersDetailsView,
                    CreateProductView, UpdateProductView,
                    DeleteProductView, CreateOrderView,
                    UpdateOrderView, DeleteOrderView)

app_name = "shopapp"

urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("groups/", GroupsListView.as_view(), name="groups_list"),
    
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/create/", CreateProductView.as_view(), name="create_product"),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name="products_details"),
    path("products/<int:pk>/update", UpdateProductView.as_view(), name="product_update"),
    path("products/<int:pk>/delete", DeleteProductView.as_view(), name="product_delete"),
    
    path("orders/", OrdersListView.as_view(), name="orders_list"),
    path("orders/create/", CreateOrderView.as_view(), name="create_order"),
    path("orders/<int:pk>/", OrdersDetailsView.as_view(), name="order_details"),
    path("orders/<int:pk>/update", UpdateOrderView.as_view(), name="order_update"),
    path("orders/<int:pk>/delete", DeleteOrderView.as_view(), name="order_delete"),
]
