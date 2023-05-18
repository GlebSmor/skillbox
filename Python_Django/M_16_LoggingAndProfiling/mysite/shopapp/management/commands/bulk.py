from django.core.management import BaseCommand

from shopapp.models import  Product

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        info = []
        
        for i in range(1000):
           info.append((f'Smartphone{i}', i + 100))
           
        products = [
            Product(name=name, price=price)
            for name, price in info
        ]
        result = Product.objects.bulk_create(products)
        
        for o in result:
            print(o)
        # res = Product.objects.filter(
        #     name__contains="Smartphone"
        # ).delete()
        
        # print(res)