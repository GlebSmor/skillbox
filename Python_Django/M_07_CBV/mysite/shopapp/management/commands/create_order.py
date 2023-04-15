from django.core.management import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Order

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create order")
        user = User.objects.get(username="gleb")
        order = Order.objects.get_or_create(
            dilivery_adress="ul Pushkina, d 5",
            promocode="SALE123",
            user=user,
        )
        self.stdout.write(f"Create order {order}")