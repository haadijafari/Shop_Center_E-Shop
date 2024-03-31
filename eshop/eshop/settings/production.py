from eshop.settings.settings import *

ALLOWED_HOSTS = [
    'https://example.com',
]

ALLOWED_HOSTS = [
    'haadijafari.ir',
    'hadijafari.info',
]

MIDDLEWARE += [
    'csp.middleware.CSPMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['SQL_NAME'],
        'USER': os.environ['SQL_USER'],
        'PASSWORD': os.environ['SQL_PASS'],
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

# reCaptcha
RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY_V2']
RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY_V2']
# RECAPTCHA_DOMAIN = 'www.recaptcha.net'
RECAPTCHA_REQUIRED_SCORE = 0.75

STATIC_ROOT = '/home/[USER]/public_html/static'
MEDIA_ROOT = '/home/[USER]/public_html/media'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
