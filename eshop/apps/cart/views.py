from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpRequest
from django.template.loader import render_to_string
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, created = Cart.objects.get_or_create(user=self.request.user, is_paid=False)

        context['sum'] = cart.calculate_total_price()
        context['tax'] = cart.calculate_tax_price()

        return context


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


def remove_cart_detail(request):
    item_id = request.GET.get('item_id')
    if item_id is None:
        return JsonResponse({
            'status': 'not_found_item_id'
        })

    deleted_count = CartDetail.objects.filter(id=item_id, cart__is_paid=False,
                                              cart__user_id=request.user.id).delete()[0]
    if deleted_count == 0:
        return JsonResponse({
            'status': 'item_not_found'
        })

    current_cart: Cart = Cart.objects.prefetch_related('cartdetail_set').get_or_create(is_paid=False,
                                                                                       user_id=request.user.id)[0]
    context = {
        'items': current_cart.cartdetail_set.all(),
        'sum': current_cart.calculate_total_price(),
        'tax': current_cart.calculate_tax_price(),
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('cart/cart_items.html', context)
    })


def change_cart_detail_count(request: HttpRequest):
    item_id = request.GET.get('item_id')
    state = request.GET.get('state')
    if item_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_or_state'
        })

    cart_detail = CartDetail.objects.filter(id=item_id, cart__user_id=request.user.id,
                                            cart__is_paid=False).first()

    if cart_detail is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    if state == 'increase':
        cart_detail.count += 1
        cart_detail.save()
    elif state == 'decrease':
        if cart_detail.count == 1:
            cart_detail.delete()
        else:
            cart_detail.count -= 1
            cart_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid'
        })

    current_cart: Cart = Cart.objects.prefetch_related('cartdetail_set').get_or_create(is_paid=False,
                                                                                       user_id=request.user.id)[0]
    context = {
        'items': current_cart.cartdetail_set.all(),
        'sum': current_cart.calculate_total_price(),
        'tax': current_cart.calculate_tax_price(),
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('cart/cart_items.html', context)
    })
