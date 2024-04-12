from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    subject = models.CharField(_('موضوع'), max_length=300)
    full_name = models.CharField(_('نام و نام خانوادگی'), max_length=200)
    email = models.EmailField(_('ایمیل'), max_length=300)
    message = models.TextField(_('متن پیام'))
    response = models.TextField(_('متن پاسخ'), null=True, blank=True)
    created_date = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True)
    is_read_by_admin = models.BooleanField(_('خوانده شده توسط ادمین'), default=False)

    def __str__(self):
        return f'{self.subject} | {self.full_name}'

    class Meta:
        verbose_name = _('پیام')
        verbose_name_plural = _('پیام ها')

