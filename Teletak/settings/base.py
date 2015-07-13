# -*- encoding: utf-8 -*-

from unipath import Path


BASE_DIR = Path(__file__).ancestor(3)

SECRET_KEY = 'ixk9=(8f_#s^kcdlhz-8c6o^^zm@nrvm4%ng-k#^fx022f45&w'

DJANGO_APPS = (

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'smart_selects',
)

LOCAL_APPS = (
    'apps.usuarios',
    'apps.almacen',
    'apps.productos',
)

THIRD_PARTY_APPS = (
    'PIL',

)


INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Teletak.urls'

WSGI_APPLICATION = 'Teletak.wsgi.application'

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

AUTH_USER_MODEL = 'usuarios.User'

LOGIN_URL = '/login'


