from django.shortcuts import render, redirect

from apps.contact.forms import ContactModelForm
from django.urls import reverse
from django.views import View
from django.views.generic import FormView


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactModelForm
    success_url = reverse('contact:contact')

    def form_valid(self, form):
        form.save()
        return super(ContactView, self).form_valid(form)
