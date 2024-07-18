from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'cart/cart.html'
