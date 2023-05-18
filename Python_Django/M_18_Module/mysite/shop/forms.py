from django import forms
from .models import Order
from bonuses.models import Profile
from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = _("user"), _("products"), _("dilivery_adress"), _("promocode")
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = _("balance")