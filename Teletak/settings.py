
# -*- encoding: utf-8 -*-

from .settingswrap.base import *

import os
import dj_database_url

DATABASES = {}

DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django_postgrespool'

STATIC_URL = '/static/'



STATIC_ROOT = 'static'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), "static"),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEBUG = True

ALLOWED_HOSTS = []