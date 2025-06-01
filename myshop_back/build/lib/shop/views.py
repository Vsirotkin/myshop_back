# shop/views.py

from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = "shop/product/list.html"
    context_object_name = "products"
    paginate_by = 12  # По желанию — пагинация

    def get_queryset(self):
        queryset = Product.objects.filter(available=True)
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get("category_slug")
        context["category"] = (
            Category.objects.filter(slug=category_slug).first()
            if category_slug
            else None
        )
        context["categories"] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product/detail.html"
    context_object_name = "product"

    def get_queryset(self):
        return Product.objects.filter(available=True)
