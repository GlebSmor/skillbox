from django.test import TestCase
from django.urls import reverse


class GetCookieViewTestCase(TestCase):
    def test_get_coockie(self):
        response = self.client.get(reverse("myauth:get-cookie"))
        self.assertContains(response, "Cookie value")
        
        
class FooBarViewTestCase(TestCase):
    def test_foo_bar(self):
        response = self.client.get(reverse("myauth:foo-bar"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['content-type'], 'application/json',)
        expected_data = {"foo": "bar", "spam": "eggs"}
        self.assertJSONEqual(response.content, expected_data)
        
