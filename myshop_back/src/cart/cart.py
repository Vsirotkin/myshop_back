# cart/cart.py

from decimal import Decimal
from django.conf import settings
from cart.forms import CartAddProductForm
from shop.models import Product


class Cart:
    def __init__(self, request=None):
        if request:
            self.session = request.session
            cart = self.session.get(settings.CART_SESSION_ID)
        else:
            self.session = {}
            cart = {}

        if not cart:
            cart = {}
            if request:
                self.session[settings.CART_SESSION_ID] = cart

        self.cart = cart

    def __iter__(self):
        product_ids = [k for k in self.cart.keys() if k.isdigit()]
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            item = cart[str(product.id)]
            item['product'] = product
            item['total_price'] = Decimal(item['price']) * item['quantity']
            item['form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}

        if update_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    def get_item_count(self):
        return sum(item["quantity"] for item in self.cart.values())
