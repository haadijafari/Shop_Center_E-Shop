from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from apps.cart.models import Cart, CartDetail
from apps.product.models import Product


class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart/cart.html'


def add_product(request):
    if request.method == 'GET':
        pid = request.GET.get('product_id')
        if request.user.is_authenticated:
            cart, created_status = Cart.objects.get_or_create(user=request.user, is_paid=False)
            product = Product.objects.filter(id=pid, is_active=True, is_delete=False).first()
            if cart_item := cart.cartdetail_set.filter(product=product).first():
                cart_item.count += 1
                cart_item.save()
                messages.success(request, _('تعداد محصول مورد نظر بروزرسانی شد.'))
            else:
                cart_item = CartDetail(cart=cart, product=product, count=1)
                cart_item.save()
                messages.success(request, _('محصول به سبر خرید اضافه شد.'))
            return JsonResponse({'status': 'success'})
        else:
            JsonResponse({'status': 'Not Authorized'})
