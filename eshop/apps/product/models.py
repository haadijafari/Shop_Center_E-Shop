from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager


class ProductCategory(models.Model):
    title = models.CharField(_('عنوان'), max_length=300, db_index=True)
    is_active = models.BooleanField(_('فعال/ غیرفعال'), default=False)
    is_delete = models.BooleanField(_('حذف شده / حذف نشده'), default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('دسته بندی ها')


class ProductBrand(models.Model):
    title = models.CharField(_('عنوان'), max_length=300, db_index=True)
    is_active = models.BooleanField(_('فعال/ غیرفعال'), default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('برند')
        verbose_name_plural = _('برند ها')


class Product(models.Model):
    title = models.CharField(_('عنوان'), max_length=300)
    category = models.ManyToManyField(ProductCategory, verbose_name=_('دسته بندی ها'),
                                      related_name='product_categories',
                                      null=True, blank=True)
    tag = TaggableManager(_('تگ ها'), blank=True)
    brand = models.ForeignKey(ProductBrand, verbose_name=_('برند'), null=True, blank=True, on_delete=models.SET_NULL)
    price = models.IntegerField(_('قیمت'))
    short_description = models.CharField(_('توضیحات کوتاه'), max_length=360, null=True)
    description = models.TextField(_('توضبحات'), null=True, blank=True)
    is_active = models.BooleanField(_('فعال / غیرفعال'), default=False)
    is_delete = models.BooleanField(_('حذف شده / حذف نشده'), default=False)
    slug = models.SlugField(_('اسلاگ'), default="", null=False, blank=True, db_index=True, max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = _('محصول')
        verbose_name_plural = _('محصولات')
