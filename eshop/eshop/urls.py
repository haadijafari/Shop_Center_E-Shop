from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from eshop.settings.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auths.user.urls')),
    path('', include('apps.index.urls')),
    path('products/', include('apps.product.urls')),
    path('contact/', include('apps.contact.urls')),
    path('about/', include('apps.about_us.urls')),
]

if DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
