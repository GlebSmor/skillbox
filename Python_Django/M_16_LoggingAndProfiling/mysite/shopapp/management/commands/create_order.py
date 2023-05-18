from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order, Product
from django.db import transaction
from typing import Sequence


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Create order")
        user = User.objects.get(username="admin")
        products: Sequence[Product] = Product.objects.defer("description", "price").all()
        order, created = Order.objects.get_or_create(
            delivery_address="ul Pupkina, d 8",
            promocode="SALE134",
            user=user,
        )

        for pr in products:
            order.products.add(pr)
        order.save()
        self.stdout.write(f"Created order {order}")