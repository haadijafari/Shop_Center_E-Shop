from django.shortcuts import render, redirect

from apps.contact.forms import ContactModelForm
from django.views import View


class ContactView(View):
    def get(self, request):
        contact_form = ContactModelForm()
        context = {
            'form': contact_form
        }
        return render(request, 'contact/contact.html', context)

    def post(self, request):
        contact_form = ContactModelForm(request.POST)
        if contact_form.is_valid():
            # process the data in form.cleaned_data as required
            contact_form.save()
            # redirect to a new URL:
            return redirect('index:home')
        context = {
            'form': contact_form
        }
        return render(request, 'contact/contact.html', context)


def contact_page_view(request):
    contact_form = ContactModelForm(request.POST or None)
    if request.method == 'POST':
        if contact_form.is_valid():
            # process the data in form.cleaned_data as required
            contact_form.save()
            # redirect to a new URL:
            return redirect('index:home')
    context = {
        'form': contact_form
    }
    return render(request, 'contact/contact.html', context)
