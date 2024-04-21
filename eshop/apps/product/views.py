from django.shortcuts import render

from apps.product.models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        return base_query.filter(is_active=True)


class ProductDetailsView(DetailView):
    template_name = 'product/product_details.html'
    model = Product

    def get_queryset(self):
        base_query = super(ProductDetailsView, self).get_queryset()
        return base_query.filter(is_active=True)
