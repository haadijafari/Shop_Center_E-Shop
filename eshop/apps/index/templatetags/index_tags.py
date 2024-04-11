from django import template

register = template.Library()


@register.inclusion_tag('shared/header.html')
def header():
    pass


@register.inclusion_tag('shared/footer.html')
def footer():
    pass
