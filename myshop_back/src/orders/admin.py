# orders/admin.py

from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "address",
        "postal_code",
        "city",
        "paid",
        "get_total_cost",
        "created",
        "updated",
    ]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInline]
    actions = ["mark_paid"]

    def get_total_cost(self, obj):
        return f"${obj.get_total_cost():.2f}"

    get_total_cost.short_description = "Total cost"

    def mark_paid(self, request, queryset):
        updated = queryset.update(paid=True)
        self.message_user(request, f"{updated} заказ(а) помечено(ы) как оплаченные")

    mark_paid.short_description = "Пометить как оплаченные"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "quantity", "price"]
    list_filter = ["order"]
    search_fields = ["product__name"]
