# shop/tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from .factories import CategoryFactory, ProductFactory


class ViewTests(TestCase):
    def setUp(self):
        self.category = CategoryFactory(name="Tea", slug="tea")
        self.product = ProductFactory(
            name="Green Tea", slug="green-tea", category=self.category, available=True
        )

    def test_product_list_view(self):
        response = self.client.get(reverse("shop:product_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Green Tea")
        self.assertTemplateUsed(response, "shop/product/list.html")

    def test_product_detail_view(self):
        url = reverse("shop:product_detail", args=[self.product.id, self.product.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Green Tea")
        self.assertTemplateUsed(response, "shop/product/detail.html")

    def test_product_list_by_category(self):
        response = self.client.get(
            reverse("shop:product_list_by_category", args=[self.category.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Green Tea")
        self.assertContains(response, "Tea")
