# shop/tests/factories.py

import factory
from factory.django import mute_signals
from shop.models import Category, Product


@mute_signals
class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'category{n}')
    slug = factory.Sequence(lambda n: f'slug{n}')

    class Meta:
        model = Category


@mute_signals
class ProductFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'product{n}')
    slug = factory.Sequence(lambda n: f'slug{n}')
    category = factory.SubFactory(CategoryFactory)
    price = 10.00
    available = True

    class Meta:
        model = Product