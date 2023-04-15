from django.contrib import admin
from .models import Product, Order
from .admin_mixins import ExportAsCSVMixin
from django.http import HttpRequest
from django.db.models import QuerySet

@admin.action(description="Archive products")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)
    
@admin.action(description="Unarchive products")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)
    
       
class OrderInline(admin.TabularInline):
    model = Product.orders.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    inlines = [
        OrderInline,
    ]
    list_display = "pk", "name", "desc_short", "price", "discount", "archived"
    list_display_links = "pk", "name"
    ordering = "pk",
    search_fields = "name", "pk"
    fieldsets = [
        ("Info", {
            "fields": ("name", "description"),
        }),
        ("Price options", {
            "fields": ("price", "discount"),
            "classes": ("wide", "collapse",),
        }),
        ("Extra options", {
            "fields": ("archived",),
            "classes": ("collapse",),
            "description": "Extra options. Field ''archived'' is soft for delete"
        })
    ]
    
    
    def desc_short(self, obj: Product):
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."


class ProductInline(admin.StackedInline):
    model = Order.products.through
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline
    ]
    list_display = "pk", "dilivery_adress", "promocode", "created_at", "user_verbose"
    list_display_links = "pk", "dilivery_adress"
    
    def get_queryset(self, request: HttpRequest):
        return Order.objects.select_related("user").prefetch_related("products")
    
    def user_verbose(self, obj: Order):
        return obj.user.first_name or obj.user.username
    

    