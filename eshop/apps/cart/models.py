from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.product.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('کاربر'))
    is_paid = models.BooleanField(_('وضعیت پرداخت'), default=False)
    created_date = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True)
    paid_date = models.DateTimeField(_('تاریخ پرداخت'), null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _('سبد خرید')
        verbose_name_plural = _('سبدهای خرید کاربران')

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for cart_detail in self.cartdetail_set.all():
                total_amount += cart_detail.final_price * cart_detail.count
        else:
            for cart_detail in self.cartdetail_set.all():
                total_amount += cart_detail.product.price * cart_detail.count
        return total_amount

    def calculate_tax_price(self):
        return self.calculate_total_price() * 0.09


class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=_('سبد'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('محصول'))
    final_price = models.IntegerField(_('قیمت حساب شده'), null=True, blank=True)
    count = models.IntegerField(_('تعداد'), default=1, null=False, blank=False)

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return f'{str(self.cart)} | {self.product.title}'

    class Meta:
        verbose_name = _('آیتم سبد خرید')
        verbose_name_plural = _('لیست محتویات سبدهای خرید')
