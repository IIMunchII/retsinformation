from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['localhost']

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