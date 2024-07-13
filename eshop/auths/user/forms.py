from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label=_('کلمه عبور'))
    password_confirm = forms.CharField(widget=forms.PasswordInput, label=_('تکرار کلمه عبور'))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            self.add_error('email', _("کاربر با این ایمیل قبلا ثبت نام کرده است"))
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', _('کلمه های عبور وارد شده یکسان نیستند.'))

        return cleaned_data
