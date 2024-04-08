from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager


class ProductCategory(models.Model):
    title = models.CharField(_('Title'), max_length=300, db_index=True)
    is_active = models.BooleanField(_('Active Status'), default=False)
    is_delete = models.BooleanField(_('Delete Status'), default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')


class Product(models.Model):
    title = models.CharField(_('Title'), max_length=300)
    category = models.ManyToManyField(ProductCategory, verbose_name=_('Categories'), related_name='product_categories')
    tag = TaggableManager(_('Tags'), blank=True)
    price = models.IntegerField(_('Price'))
    short_description = models.CharField(_('Short Description'), max_length=360, null=True)
    description = models.TextField(_('Main Description'), null=True, blank=True)
    is_active = models.BooleanField(_('Active Status'), default=False)
    is_delete = models.BooleanField(_('Delete Status'), default=False)
    slug = models.SlugField(_('Slug'), default="", null=False, blank=True, db_index=True, max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
