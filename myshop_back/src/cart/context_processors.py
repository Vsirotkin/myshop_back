# cart/context_processors.py


def cart_context(request):
    from cart.cart import Cart

    cart = Cart(request)

    return {"cart_items_count": len(cart), "cart_total": cart.get_total_price()}
