
# -*- encoding: utf-8 -*-

from .settingswrap.base import *



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


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEBUG = True

ALLOWED_HOSTS = []