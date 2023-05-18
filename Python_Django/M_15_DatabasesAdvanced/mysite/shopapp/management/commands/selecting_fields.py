from django.core.management import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Order, Product

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        product_values = Product.objects.values("pk", "name")
        users_info = User.objects.values_list("username")
        print(users_info)
        for pv in product_values:
            print(pv)
        