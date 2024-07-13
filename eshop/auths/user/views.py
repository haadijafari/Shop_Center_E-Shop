from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import FormView

from .forms import RegistrationForm, LoginForm

User = get_user_model()


# todo: Error message should be handled
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


# todo: Error message should be handled
class ActivationView(View):
    def get(self, request, validation_code):
        user = get_object_or_404(User, verification_code=validation_code)
        if user.is_active:
            messages.info(request, _('حساب کاربری شما قبلا فعال شده است.'))
            return redirect(reverse('index:home'))

        user.is_active = True
        user.verification_code = get_random_string(128)
        user.save()
        messages.success(request, _('حساب کاربری شما با موفقیت فعال شد!'))
        return redirect(reverse('user:login'))


# todo: Error message should be handled
class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index:home')

    def form_valid(self, form):
        user = form.get_user()
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            messages.error(self.request, 'Invalid email or password.')
            return self.form_invalid(form)


class ForgetPassView(View):
    def get(self):
        pass


class LogoutView(View):
    def get(self):
        pass
