from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import ListView

from apps.cart.models import Cart, CartDetail
from apps.product.models import Product


class CartView(LoginRequiredMixin, ListView):
    template_name = 'cart/cart.html'
    model = CartDetail
    context_object_name = 'items'

    def get_queryset(self):
        cart, created = Cart.objects.prefetch_related('cartdetail_set').get_or_create(user=self.request.user,
                                                                                      is_paid=False)
        return CartDetail.objects.filter(cart=cart)


def add_product(request):
    if request.method == 'GET':
        pid = request.GET.get('product_id')
        if request.user.is_authenticated:
            cart, created_status = Cart.objects.get_or_create(user=request.user, is_paid=False)
            product = Product.objects.filter(id=pid, is_active=True, is_delete=False).first()
            if cart_item := cart.cartdetail_set.filter(product=product).first():
                cart_item.count += 1
                cart_item.save()
            else:
                cart_item = CartDetail(cart=cart, product=product, count=1)
                cart_item.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'not_authorized'})
