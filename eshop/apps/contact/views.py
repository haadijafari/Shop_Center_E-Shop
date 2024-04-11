from django.shortcuts import render


def contact_page_view(request):
    return render(request, 'contact/contact.html')
