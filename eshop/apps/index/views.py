from django.shortcuts import render
from django.views.generic import TemplateView

from apps.product.models import Product
from apps.site_settings.models import Slider
from utils.convertors import list_grouper


def home_page_view(request):
    return render(request, 'index/index.html')


class HomeView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['sliders'] = Slider.objects.filter(is_active=True)
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        context['latest_products'] = list_grouper(latest_products)
        return context
