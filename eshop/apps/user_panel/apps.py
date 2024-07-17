from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UserPanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user_panel'
    verbose_name = _('پنل کاربری')
