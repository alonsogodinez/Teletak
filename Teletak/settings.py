
# -*- encoding: utf-8 -*-

from .settingswrap.base import *

import os
import dj_database_url

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
# DATABASES['default'] =  dj_database_url.config()
# DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

STATIC_URL = '/static/'



STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'Teletak/static'),
    os.path.join(BASE_DIR, 'Teletak/static/css'),
    os.path.join(BASE_DIR, 'Teletak/static/js'),
    os.path.join(BASE_DIR, 'Teletak/static/fonts'),
    os.path.join(BASE_DIR, 'Teletak/static/img'),

)


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEBUG = True

ALLOWED_HOSTS = []