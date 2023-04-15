from django.core import validators
from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount"
        
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "user", "products", "dilivery_adress", "promocode"