from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AboutUsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.about_us'
    verbose_name = _('درباره ما')
