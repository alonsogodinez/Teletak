__author__ = 'kevin'

from .base import *




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'teletak',
        'USER': 'postgres',
        'PASSWORD': '745522',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR.child('static')]

DEBUG = True

ALLOWED_HOSTS = []
