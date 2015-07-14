
from .base import *




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'teletak2',
        'USER': 'Alonso',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '',
    }
}



STATIC_URL = '/static/'



STATICFILES_DIRS = [BASE_DIR.child('static')]

DEBUG = True

ALLOWED_HOSTS = []