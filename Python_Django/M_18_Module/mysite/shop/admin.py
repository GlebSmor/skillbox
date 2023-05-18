from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = "pk", "name", "price"
    list_display_links = ["pk", "name"]
    ordering = ["pk",]
    
    
@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = "pk", "delivery_address", "created_at"
    list_display_links = ["pk",]
    ordering = ["pk",]
