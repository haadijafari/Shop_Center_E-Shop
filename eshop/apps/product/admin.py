from django.contrib import admin

from apps.product.models import Product, ProductCategory, ProductBrand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug', ]
    prepopulated_fields = {
        'slug': ['title']
    }
    list_filter = ['category', 'is_active']
    list_display = ['__str__', 'price', 'is_active', 'is_delete']
    list_editable = ['price', 'is_active']


admin.site.register(ProductCategory)
admin.site.register(ProductBrand)
