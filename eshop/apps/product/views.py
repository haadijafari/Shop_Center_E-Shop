from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from apps.cart.models import Cart, CartDetail
from apps.product.models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 10

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        return base_query.filter(is_active=True)


class ProductDetailsView(DetailView):
    template_name = 'product/product_details.html'
    model = Product

    def get_queryset(self):
        base_query = super(ProductDetailsView, self).get_queryset()
        return base_query.filter(is_active=True)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        # Add Item to Cart
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user, is_paid=False).first()
            if cart is None:
                cart = Cart(user=request.user)
                cart.save()
            product = Product.objects.filter(id=kwargs.get('pid'), is_active=True, is_delete=False).first()
            cart_item = cart.cartdetail_set.filter(product=product).first()
            context['cart_item'] = cart_item
            if count := request.GET.get('count'):
                if cart_item:
                    cart_item.count = count
                    cart_item.save()
                    messages.success(request, _('تعداد محصول مورد نظر بروزرسانی شد.'))
                else:
                    cart_item = CartDetail(cart=cart, product=product, count=count)
                    cart_item.save()
                    messages.success(request, _('محصول به سبر خرید اضافه شد.'))
        # else:
        #     context['cart_item'] = None
        return self.render_to_response(context)
