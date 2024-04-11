from django.shortcuts import render

from apps.product.models import Product


def product_list_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'product/product_list.html', context)


def product_details_view(request, pid, slug):
    context = {
        'product': Product.objects.get(id=pid, slug=slug)
    }
    print(context)
    return render(request, 'product/product_details.html', context)
