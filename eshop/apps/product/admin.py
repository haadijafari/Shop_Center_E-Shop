from django.contrib import admin

from apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug', ]
    prepopulated_fields = {
        'slug': ['title']
    }
    list_filter = ['is_active']
    list_display = ['__str__', 'price', 'is_active']
    list_editable = ['is_active']

# admin.site.register(Product, ProductAdmin)
