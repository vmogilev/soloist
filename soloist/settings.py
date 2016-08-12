"""
Django settings for soloist project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv('DJANGO_DEBUG', False))

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'soloist.apps.portals.apps.PortalsConfig',
    'soloist.apps.clients.apps.ClientsConfig',
    'soloist.apps.categories.apps.CategoriesConfig',
    'soloist.apps.projects.apps.ProjectsConfig',
    'soloist.apps.worklogs.apps.WorklogsConfig',
    'soloist.apps.search.apps.SearchConfig',
    'soloist.apps.uploads.apps.UploadsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'lib.require_login_middleware.RequireLoginMiddleware',
]

ROOT_URLCONF = 'soloist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
            'libraries': {
                'breadcrumbs': 'lib.breadcrumbs',
            },
        },
    },
]

WSGI_APPLICATION = 'soloist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DJANGO_SOLOIST_DB_NAME', 'scdb'),
        'USER': os.getenv('DJANGO_SOLOIST_DB_USER', 'scapp'),
        'PASSWORD': os.getenv('DJANGO_SOLOIST_DB_PASS', 'scapp'),
        'HOST': os.getenv('DJANGO_SOLOIST_DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DJANGO_SOLOIST_DB_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        # },
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'deploy/static')


# Elasticsearch
# http://elasticsearch-dsl.readthedocs.io/en/latest/configuration.html
# http://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch
# https://github.com/HonzaKral/es-django-example/

ES_INDEX = os.getenv('ES_INDEX', 'soloist')

ES_CONNECTIONS = {
    'default': {
        'hosts': os.getenv('ES_HOST', 'localhost:9200'),
        'use_ssl': bool(os.getenv('ES_USE_SSL', False)),
        'sniff_on_start': True,
        'sniff_on_connection_fail': True,
        'sniffer_timeout': 60,
    },
}


# S3 Uploads

S3_UPLOAD_BUCKET = os.getenv('S3_UPLOAD_BUCKET')
S3_UPLOAD_PREFIX = os.getenv('S3_UPLOAD_PREFIX')


# see lib/require_login_middleware.py

LOGIN_REQUIRED_URLS = (
        r'/(.*)$',
    )
LOGIN_REQUIRED_URLS_EXCEPTIONS = (
    r'/login(.*)$',
    r'/logout(.*)$',
)

LOGIN_URL = '/login/'


# Soloist Template Settings (exported via django_settings_export.settings_export)

SOLOIST_TITLE = os.getenv('SOLOIST_TITLE', "Soloist")
SOLOIST_DESCR = os.getenv('SOLOIST_DESCR', "Soloist helps freelancers get paid by providing \
daily status updates to their clients.")
SOLOIST_BRAND = os.getenv('SOLOIST_BRAND', "Soloist")

SETTINGS_EXPORT_VARIABLE_NAME = 'soloist'
SETTINGS_EXPORT = [
    'SOLOIST_TITLE',
    'SOLOIST_DESCR',
    'SOLOIST_BRAND',
]
