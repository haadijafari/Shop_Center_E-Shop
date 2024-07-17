from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    verification_code = models.CharField(
        _('Verification Code'),
        max_length=128,
        default=get_random_string(128),
        editable=False,
        blank=False,
        null=False,
        db_index=True,
    )
    avatar = models.ImageField(_('عکس پروفایل'), upload_to='Images/user/avatar', null=True, blank=True)
    about = models.TextField(_('درباره من'), null=True, blank=True)
    address = models.TextField(_('آدرس'), null=True, blank=True)

    class Meta:
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربران')
