from django.contrib import admin
from .models import AboutUs, SiteSetting, FooterLinkBox, FooterLink, Slider


@admin.register(AboutUs)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['is_main_setting']
    list_display = ['__str__', 'phone', 'email', 'is_main_setting']
    list_editable = ['is_main_setting']


@admin.register(SiteSetting)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ['is_main_setting']
    list_display = ['__str__', 'is_main_setting']
    list_editable = ['is_main_setting']


admin.site.register(FooterLinkBox)
admin.site.register(FooterLink)
admin.site.register(Slider)
