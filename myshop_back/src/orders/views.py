# orders/views.py

from django.views import View
from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart


class OrderCreateView(View):
    template_name = "orders/order/create.html"
    success_template = "orders/order/created.html"

    def get(self, request):
        cart = Cart(request)
        form = OrderCreateForm()
        return render(request, self.template_name, {"cart": cart, "form": form})

    def post(self, request):
        cart = Cart(request)

        # 🔥 Проверка на пустую корзину
        if len(cart) == 0:
            form = OrderCreateForm(request.POST)
            form.add_error(None, "Ваша корзина пуста. Невозможно оформить заказ.")
            return render(request, self.template_name, {"cart": cart, "form": form})

        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )

            cart.clear()
            return render(request, self.success_template, {"order": order})

        return render(request, self.template_name, {"cart": cart, "form": form})
