# tests/test_cart.py

from cart import Cart
from unittest.mock import Mock


def test_add_product_to_cart():
    session = {"cart": {}, "modified": False}
    mock_request = Mock(session=session)

    cart = Cart(mock_request.session)
    product = Mock(id=1, price=Decimal("10.00"))
    cart.add(product, 2)

    assert session["cart"]["1"]["quantity"] == 2
    assert session["cart"]["1"]["price"] == "10.00"
