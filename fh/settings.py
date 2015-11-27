"""
Django settings for fh project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = (
    'autocomplete_light',
    'suit',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'debug_toolbar',
    'django_extensions',
    'stronghold',
    'crispy_forms',
    'sitetree',
    'widget_tweaks',
    'taggit',
    'compressor',
    'avatar',

    # Fh apps
    'fh',
    'users',
    'finances',
    'analytics'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'fh.middleware.WhodidMiddleware',
    'fh.middleware.UserMiddleware',
    'stronghold.middleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'fh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'fh/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SITE_ID = 1

WSGI_APPLICATION = 'fh.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'fh/static'),
    os.path.join(BASE_DIR, 'bower_components'),
    )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 600
    }
}

# Django-suit
SUIT_CONFIG = {
    'ADMIN_NAME': 'FamilyHelper',
    'MENU': (
        {'app': 'auth', 'label': 'Users', 'icon': 'icon-user', 'models': ('auth.user', 'avatar.avatar', 'auth.group')},
        {'app': 'finances', 'icon': 'icon-briefcase'},
        {'label': 'Navigation', 'icon': 'icon-list',
         'models': ('fh.sitetreetree', 'taggit.tag', 'sites.site')},
    ),
    'LIST_PER_PAGE': 20
}

# Django stronghold
STRONGHOLD_DEFAULTS = True

STRONGHOLD_PUBLIC_URLS = (
    r'^/admin.+$',
)

STRONGHOLD_PUBLIC_NAMED_URLS = (
    'django.contrib.auth.views.login',
)

# Django sitetree
SITETREE_MODEL_TREE_ITEM = 'fh.SiteTreeItem'
SITETREE_MODEL_TREE = 'fh.SiteTreeTree'

# Django avatar
AVATAR_GRAVATAR_DEFAULT = 'mm'

# Django crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Local settings
try:
    from fh.local_settings import *
except ImportError:
    pass

if not DEBUG:
    AUTHENTICATION_BACKENDS = (
        'ratelimitbackend.backends.RateLimitModelBackend',
    )
