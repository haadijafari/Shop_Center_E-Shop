from django.shortcuts import render


# Create your views here.
def product_list_view(request):
    return render(request, 'product/product_list.html')


def product_details_view(request):
    return render(request, 'product/product_details.html')
