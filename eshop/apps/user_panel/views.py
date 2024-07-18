from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from auths.user.models import User
from .forms import UserProfileModelForm


class UserPanel(LoginRequiredMixin, TemplateView):
    template_name = 'user_panel/user_panel_dashboard.html'


class EditProfileInfo(LoginRequiredMixin, UpdateView):
    template_name = 'user_panel/user_panel_edit_profile.html'
    model = User
    form_class = UserProfileModelForm
    success_url = reverse_lazy('user_panel:edit_profile')

    def get_object(self, queryset=None):
        return self.request.user


class ChangePass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user_panel/user_panel_change_password.html'
    success_url = reverse_lazy('user:login')
