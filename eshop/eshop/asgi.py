"""
ASGI config for eshop project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from eshop.settings.settings import DEBUG

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eshop.settings.production')

application = get_asgi_application()
