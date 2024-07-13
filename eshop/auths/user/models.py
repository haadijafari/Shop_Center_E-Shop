from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    verification_code = models.CharField(
        max_length=128,
        default=get_random_string(128),
        editable=False,
        blank=False,
        null=False,
        db_index=True,
    )

    class Meta:
        verbose_name = _('کاربر')
        verbose_name_plural = _('کاربران')
