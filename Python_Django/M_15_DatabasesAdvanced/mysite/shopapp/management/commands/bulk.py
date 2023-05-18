from django.core.management import BaseCommand

from shopapp.models import  Product

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # info = {
        #     ("Smartphone1", 199),
        #     ("Smartphone2", 299),
        #     ("Smartphone3", 399),
        # }
        
        # products = [
        #     Product(name=name, price=price)
        #     for name, price in info
        # ]
        # result = Product.objects.bulk_create(products)
        
        # for o in result:
            # print(o)
        res = Product.objects.filter(
            name__contains="Smartphone"
        ).delete()
        
        print(res)