# shop/tests/test_templates.py

from django.test import TestCase
from django.urls import reverse
from shop.models import Category, Product


class TemplateTests(TestCase):
    def test_product_list_uses_correct_template(self):
        """Проверяет, что список товаров использует правильный шаблон"""
        response = self.client.get(reverse("shop:product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/product/list.html")

    def test_product_detail_uses_correct_template(self):
        """Проверяет, что детальная страница товара использует правильный шаблон"""
        category = Category.objects.create(name="Tea", slug="tea")
        product = Product.objects.create(
            name="Green Tea", slug="green-tea", category=category, price=5.99
        )
        url = reverse("shop:product_detail", args=[product.id, product.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/product/detail.html")
