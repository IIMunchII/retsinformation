from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['retsinfosoegning.dk', 'www.retsinfosoegning.dk']
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': '8f5e650382c04ffdb1752d531cca9885',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Redis settings
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_USER = "django"