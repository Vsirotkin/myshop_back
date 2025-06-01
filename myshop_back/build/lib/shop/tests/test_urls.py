# shop/tests/test_urls.py

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import ProductListView, ProductDetailView


class UrlTests(SimpleTestCase):
    def test_product_list_url_resolves(self):
        url = reverse("shop:product_list")
        self.assertEqual(resolve(url).func.view_class, ProductListView)

    def test_product_list_by_category_url_resolves(self):
        url = reverse("shop:product_list_by_category", args=["tea"])
        self.assertEqual(resolve(url).func.view_class, ProductListView)

    def test_product_detail_url_resolves(self):
        url = reverse("shop:product_detail", args=[1, "tea"])
        self.assertEqual(resolve(url).func.view_class, ProductDetailView)
