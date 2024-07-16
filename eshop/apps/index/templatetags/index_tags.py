from django import template
from apps.site_settings.models import FooterLinkBox, AboutUs, SiteSetting

register = template.Library()


@register.inclusion_tag('shared/header.html', takes_context=True)
def header(context):
    return {
        'site_settings': SiteSetting.objects.filter(is_main_setting=True).first(),
        'request': context['request'],
    }


@register.inclusion_tag('shared/footer.html', takes_context=True)
def footer(context):
    return {
        'site_settings': SiteSetting.objects.filter(is_main_setting=True).values('site_title', 'copy_right').first(),
        'about': AboutUs.objects.filter(is_main_setting=True).first(),
        'footer_link_boxs': FooterLinkBox.objects.filter(is_active=True),
    }
