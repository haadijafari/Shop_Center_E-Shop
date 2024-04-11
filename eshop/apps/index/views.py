from django.shortcuts import render


def home_page_view(request):
    return render(request, 'index/index.html')


def contact_page_view(request):
    return render(request, 'index/contact.html')
