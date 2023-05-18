from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _, ngettext


class Product(models.Model):
    """
    Модель Product
    
    Заказы тут: :model:`shopapp.Order`
    """
    class Meta:
        ordering = ["name", "price"]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=False, blank=True, db_index=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return f"Product(pk={self.pk}, name={self.name!r})"


class Order(models.Model):
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        
    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=20, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")
    receipt = models.FileField(null=True, upload_to='orders/receipts')
