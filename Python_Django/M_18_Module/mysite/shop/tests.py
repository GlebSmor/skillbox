from django.test import TestCase
from .views import Order, Product
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User


class OrderDetailViewTestCase(TestCase):
    
    fixtures = [
        'products-fixture.json',
        'orders-fixture.json',
        'users-fixture.json',
        
    ]
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.credentials = dict(username="bob", password="pass")
        cls.user = User.objects.create_user(**cls.credentials)
        
    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client.force_login(self.user)
        self.order = Order.objects.create(
            delivery_address= "Ul. Pushkina d.7",
            promocode="Sales123",
            user=self.user
        )
        
    def tearDown(self):
        self.order.delete()
        
    def test_order_details(self):
        response = self.client.get(
            reverse("shop:order_detail", kwargs={"pk": self.order.pk})
        )
        print(response.content)
        self.assertContains(response, self.order.delivery_address)
        self.assertContains(response, self.order.promocode)
        self.assertEqual(response.context['order'].pk, self.order.pk)
        
        
class ProductDetailsViewTestCase(TestCase):
        @classmethod
        def setUpClass(cls):
            cls.product = Product.objects.create(name="Test_Product")
          
        @classmethod  
        def tearDownClass(cls):
            cls.product.delete()
            
        def test_get_product(self):
            response = self.client.get(
                reverse("shop:product_detail", kwargs={"pk": self.product.pk})
            )
            self.assertEqual(response.status_code, 200)
            
        def test_get_product_and_check_content(self):
            response = self.client.get(
                reverse("shop:product_detail", kwargs={"pk": self.product.pk})
            )
            self.assertContains(response, self.product.name)
 
  
