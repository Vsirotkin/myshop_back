# orders/urls.py

from django.urls import path
from orders.views import *

app_name = "orders"

urlpatterns = [
    path("", OrderCreateView.as_view(), name="order_create"),
]
