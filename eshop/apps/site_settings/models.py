from django.db import models
from django.utils.translation import gettext_lazy as _


class SiteSetting(models.Model):
    site_title = models.CharField(_('عنوان سایت'), max_length=128)
    copy_right = models.TextField(_('متن کپی رایت سایت'))
    logo = models.ImageField(_('لوگو'), upload_to='images/settings/logo')
    is_main_setting = models.BooleanField(_('تنظیمات اصلی'), default=False)

    class Meta:
        verbose_name = _('کانفیگ تنظیمات پایه')
        verbose_name_plural = _('کانفیگ های تنظیمات پایه')

    def __str__(self):
        return self.site_name


class AboutUs(models.Model):
    about_us_title = models.CharField(_('عنوان'), max_length=128)
    address = models.CharField(_('آدرس'), max_length=512, null=True, blank=True)
    phone = models.CharField(_('شماره تماس'), max_length=100, null=True, blank=True)
    fax = models.CharField(_('فکس'), max_length=128, null=True, blank=True)
    email = models.CharField(_('ایمیل'), max_length=128, null=True, blank=True)
    about_us_text = models.TextField(_('متن درباره ما سایت'))
    is_main_setting = models.BooleanField(_('تنظیمات اصلی'), default=False)

    class Meta:
        verbose_name = _('درباره ما')
        verbose_name_plural = _('مشخصات درباره ما')

    def __str__(self):
        return self.about_us_title


class FooterLinkBox(models.Model):
    title = models.CharField(_('عنوان'), max_length=200)
    is_active = models.BooleanField(_('فعال / غیرفعال'), default=True)

    class Meta:
        verbose_name = _('دسته بندی لینک های فوتر')
        verbose_name_plural = _('دسته بندی های لینک های فوتر')

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(_('عنوان'), max_length=128)
    url = models.URLField(_('لینک'), max_length=512)
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name=_('دسته بندی'))
    is_active = models.BooleanField(_('فعال / غیرفعال'), default=True)

    class Meta:
        verbose_name = _('لینک فوتر')
        verbose_name_plural = _('لینک های فوتر')

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(_('عنوان'), max_length=128)
    url = models.URLField(_('لینک'), max_length=512)
    url_title = models.URLField(_('عنوان لینک'), max_length=128)
    description = models.TextField(_('توضیحات اسلایدر'))
    image = models.ImageField(_('تصویر اسلایدر'), upload_to='images/sliders')
    is_active = models.BooleanField(_('فعال / غیرفعال'), default=True)

    class Meta:
        verbose_name = _('اسلایدر')
        verbose_name_plural = _('اسلایدر ها')

    def __str__(self):
        return self.title
