from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import FormView

from .forms import RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm

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
    def get(self, request, verification_code):
        user: User = get_object_or_404(User, verification_code=verification_code)
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


# todo: Error message should be handled
class ForgotPasswordView(FormView):
    template_name = 'user/forgot_password.html'
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user: User = get_object_or_404(User, email__iexact=email)
        # Generate a unique password reset token and send an email to the user
        # Here, you would typically use Django's built-in password reset functionality
        # todo: send email with user.verification_code
        print(user.verification_code)

        return super().form_valid(form)


class ResetPasswordView(View):
    def get(self, request, verification_code):
        user = get_object_or_404(User, verification_code__iexact=verification_code)

        form = ResetPasswordForm()

        context = {
            'form': form,
            'user': user
        }
        return render(request, 'user/reset_password.html', context)

    def post(self, request, verification_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(verification_code__iexact=verification_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('user:login'))
            user_new_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('user:login'))

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }

        return render(request, 'user/login.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('user:login'))
