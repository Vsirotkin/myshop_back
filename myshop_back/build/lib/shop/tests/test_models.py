# shop/tests/test_models.py

from django.test import TestCase
from .factories import CategoryFactory, ProductFactory


class ModelTests(TestCase):
    def test_category_creation(self):
        category = CategoryFactory(name="Tea", slug="tea")
        self.assertEqual(category.name, "Tea")
        self.assertEqual(str(category), "Tea")

    def test_product_creation(self):
        product = ProductFactory(name="Green Tea", price=5.99, available=True)
        self.assertEqual(product.price, 5.99)
        self.assertTrue(product.available)
        self.assertEqual(str(product), "Green Tea")
