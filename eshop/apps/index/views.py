from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def home_page_view(request):
    return render(request, 'index/index.html')


# class HomeView(View):
#     def get(self, request):
#         return render(request, 'index/index.html')

class HomeView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        # context['request'] = self.request
        return context
