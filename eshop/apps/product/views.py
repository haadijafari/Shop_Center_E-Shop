from django.shortcuts import render

from apps.product.models import Product
from django.views.generic import TemplateView, ListView


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        return base_query.filter(is_active=True)


def product_list_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'product/product_list.html', context)


class ProductDetailsView(TemplateView):
    template_name = 'product/product_details.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailsView, self).get_context_data()
        context['product'] = Product.objects.get(id=kwargs.get('pid'), slug=kwargs.get('slug'))
        return context


def product_details_view(request, pid, slug):
    context = {
        'product': Product.objects.get(id=pid, slug=slug)
    }
    print(context)
    return render(request, 'product/product_details.html', context)
