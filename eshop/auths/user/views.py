from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import FormView

from .forms import RegistrationForm


class RegistrationView(FormView):
    template_name = 'user/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('index:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.is_active, user.is_superuser, user.is_staff = False, False, False
        user.save()
        # todo: Send Email and Wait for verification
        return super().form_valid(form)


class ActivationView(View):
    def get(self):
        pass


class LoginView(View):
    def get(self):
        pass


class ForgetPassView(View):
    def get(self):
        pass


class LogoutView(View):
    def get(self):
        pass
