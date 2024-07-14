from django import template

register = template.Library()


@register.inclusion_tag('shared/header.html', takes_context=True)
def header(context):
    return {
        "request": context["request"],
    }


@register.inclusion_tag('shared/footer.html')
def footer():
    pass
