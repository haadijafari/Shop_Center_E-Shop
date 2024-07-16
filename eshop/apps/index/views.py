from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from apps.site_settings.models import Slider, FooterLink


def home_page_view(request):
    return render(request, 'index/index.html')


class HomeView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['sliders'] = Slider.objects.filter(is_active=True)
        return context
