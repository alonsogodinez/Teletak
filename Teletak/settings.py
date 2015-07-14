
# -*- encoding: utf-8 -*-

from .settingswrap.base import *

import os

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




STATIC_ROOT = 'static'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), "static"),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEBUG = True

ALLOWED_HOSTS = []