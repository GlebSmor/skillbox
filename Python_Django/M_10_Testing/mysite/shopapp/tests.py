from string import ascii_letters
from random import choices
from .models import Product, Order
from django.test import TestCase
from django.urls import reverse
from .utils import plus
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import Permission

class PlusTestCase(TestCase):
    def test_plus(self):
        result = plus(3, 5)
        self.assertEqual(result, 8)
        
        
class ProductCreateTestCase(TestCase):
    def setUp(self):
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()
    def test_create_product(self):
        response = self.client.post(
            reverse("shopapp:product_create"),
            {
                "name": self.product_name, 
                "price": "123.46", 
                "description": "best table", 
                "discount": "10",
            }
        )
        self.assertRedirects(response, reverse("shopapp:products_list"))
        self.assertTrue(Product.objects.filter(name=self.product_name).exists())
        
        
class ProductDetailsViewTestCase(TestCase):
        @classmethod
        def setUpClass(cls):
            cls.product = Product.objects.create(name="Best Product")
          
        @classmethod  
        def tearDownClass(cls):
            cls.product.delete()
            
        def test_get_product(self):
            response = self.client.get(
                reverse("shopapp:product_details", kwargs={"pk": self.product.pk})
            )
            self.assertEqual(response.status_code, 200)
            
        def test_get_product_and_check_content(self):
            response = self.client.get(
                reverse("shopapp:product_details", kwargs={"pk": self.product.pk})
            )
            self.assertContains(response, self.product.name)
        
        
class ProductListViewTestCase(TestCase):
    fixtures = [
        'products-fixture.json'
    ]
    
    def test_products(self):
        response = self.client.get(reverse("shopapp:products_list"))
        self.assertQuerysetEqual(
            qs=Product.objects.filter(archived=False).all(),
            values=(p.pk for p in response.context["products"]),
            transform=lambda p: p.pk,
        )
        self.assertTemplateUsed(response, 'shopapp/products-list.html')
        
        
class OrdersListViewTestCase(TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.credentials = dict(username="bob", password="pass")
        cls.user = User.objects.create_user(**cls.credentials)
        
    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        
    def setUp(self):
        self.client.login(**self.credentials)
        
    def test_orders_view(self):
        response = self.client.get(reverse("shopapp:order_list"))
        self.assertContains(response, "Orders")
        
    def test_orders_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse("shopapp:order_list"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)
        
        
class ProductsExportViewTestCase(TestCase):
    fixtures = [
        'products-fixture.json'
    ]
    
    def test_get_products(self):
        response = self.client.get(
            reverse("shopapp:products-export")
        )
        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by("pk").all()
        expected_data = [
            {
                "pk": pr.pk,
                "name": pr.name,
                "price": str(pr.price),
                "archived": pr.archived,
            }
            for pr in products
        ]
        products_data = response.json()
        self.assertEqual(
            products_data["products"],
            expected_data
        )
        
        
class OrderDetailViewTestCase(TestCase):
    
    fixtures = [
        'products-fixture.json'
    ]
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.credentials = dict(username="bob", password="pass")
        cls.user = User.objects.create_user(**cls.credentials)
        cls.user.user_permissions.add(Permission.objects.get(codename='view_order'))
        
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
            reverse("shopapp:order_detail", kwargs={"pk": self.order.pk})
        )
        self.assertContains(response, self.order.delivery_address)
        self.assertContains(response, self.order.promocode)
        self.assertEqual(response.context['order'].pk, self.order.pk)
        
        
class OrderExportTestCases(TestCase):
    fixtures = [
        'orders-fixture.json',
        'products-fixture.json',
        'users-fixture.json'
        
    ]
    
    
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="bob", password="pass")
        cls.user.is_staff=True
        cls.user.save()
        
    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        
    def setUp(self):
        self.client.force_login(self.user)
        
    def test_order_export(self):
        response = self.client.get(reverse("shopapp:orders-export"))
        self.assertEqual(response.status_code, 200)
        
        orders = Order.objects.order_by("pk").all()
        expected = {"orders": [
                {
                "pk": order.pk,
                "delivery_address": order.delivery_address,
                "promocode": order.promocode,
                "user": order.user.pk,
                "products": [product.pk for product in order.products.all()]    
                }
                for order in orders
            ]
            }
        
        self.assertEqual(response.json(), expected)