from django.test import TestCase
from shop.models import Category, Product


class ModelTests(TestCase):
    def test_category_creation(self):
        """Проверяет создание категории"""
        category = Category.objects.create(name="Tea", slug="tea")
        self.assertEqual(str(category), "Tea")
        self.assertEqual(category.name, "Tea")
        self.assertEqual(category.slug, "tea")

    def test_product_creation(self):
        """Проверяет создание товара"""
        category = Category.objects.create(name="Tea", slug="tea")
        product = Product.objects.create(
            name="Green Tea",
            slug="green-tea",
            category=category,
            price=5.99,
            available=True
        )
        self.assertEqual(str(product), "Green Tea")
        self.assertEqual(product.price, 5.99)
        self.assertTrue(product.available)
        self.assertEqual(product.category, category)

    def test_get_absolute_url_for_category(self):
        """Проверяет get_absolute_url для категории"""
        category = Category.objects.create(name="Tea", slug="tea")
        self.assertIn("/tea/", category.get_absolute_url())

    def test_get_absolute_url_for_product(self):
        """Проверяет get_absolute_url для продукта"""
        category = Category.objects.create(name="Tea", slug="tea")
        product = Product.objects.create(
            name="Green Tea",
            slug="green-tea",
            category=category,
            price=5.99
        )
        self.assertIn("/green-tea/", product.get_absolute_url())