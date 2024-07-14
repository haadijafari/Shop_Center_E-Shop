from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data()
        # context['request'] = self.request
        return context
