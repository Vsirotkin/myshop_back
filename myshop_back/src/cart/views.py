# cart/views.py

from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from shop.models import Product
from cart.cart import Cart
from cart.forms import CartAddProductForm


@method_decorator(csrf_exempt, name="dispatch")
class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                product=product, quantity=cd["quantity"], update_quantity=cd["override"]
            )

        # AJAX запрос? → JSON
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse(
                {
                    "cart": list(cart),
                    "total_price": cart.get_total_price(),
                    "count": len(cart),
                }
            )

        return redirect("cart:cart_detail")


@method_decorator(csrf_exempt, name="dispatch")
class CartRemoveView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse(
                {
                    "success": True,
                    "removed_product_id": product_id,
                    "count": len(cart),
                    "total_price": cart.get_total_price(),
                }
            )

        return redirect("cart:cart_detail")


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse(
                {
                    "items": list(cart),
                    "total_price": cart.get_total_price(),
                    "count": len(cart),
                }
            )

        return render(request, "cart/detail.html", {"cart": cart})
