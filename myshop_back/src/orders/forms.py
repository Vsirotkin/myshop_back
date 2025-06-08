# orders/forms.py

from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "address", "postal_code", "city"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Имя"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Фамилия"}),
            "email": forms.EmailInput(attrs={"placeholder": "example@example.com"}),
            "address": forms.TextInput(attrs={"placeholder": "Адрес доставки"}),
            "postal_code": forms.TextInput(attrs={"placeholder": "123456"}),
            "city": forms.TextInput(attrs={"placeholder": "Город"}),
        }
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "email": "Email",
            "address": "Адрес",
            "postal_code": "Почтовый индекс",
            "city": "Город",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Убираем "Optional" из label
        for field in self.fields.values():
            field.required = True
