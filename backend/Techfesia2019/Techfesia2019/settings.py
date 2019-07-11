"""
Django settings for Techfesia2019 project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta
import firebase_admin

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# try importing local settings lse use public settings

try:
    from . import local_settings as external_settings
    print("Using local settings")
except:
    from . import public_settings as external_settings
    print("using public settings")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = external_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = external_settings.DEBUG

ALLOWED_HOSTS = external_settings.ALLOWED_HOSTS

# Application definition

INSTALLED_APPS = [

    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # rest apps
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'rest_framework_swagger',
    'corsheaders',

    # custom apps
    'base',
    'registration',
    'events',
    'accounts',
    'tickets',
    'event_registrations',
    'blog',
    'etc',
    'management'

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Techfesia2019.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Techfesia2019.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = external_settings.DATABASES

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'registration.User'

APPEND_SLASH = True
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Rest Framework
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': (

        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # session auth must come after jwt auth to ensure correct status codes are sent back
    )
}

# simple jwt settings

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': DEBUG and timedelta(minutes=100) or timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

}

# CORS Settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    "https://stackoverflow.com",
]


# Swagger Settings

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        "api_key": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


# login logout config
LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'

# static media dirs
STATIC_URL = '/static/'
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#    # '/var/www/static/', # to be used with nginx
#]

STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# sendgrid
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
SENDGRID_API_KEY = external_settings.SENDGRID_API_KEY

EMAIL_BACKEND = external_settings.EMAIL_BACKEND
EMAIL_HOST = external_settings.EMAIL_BACKEND
EMAIL_PORT = 587
EMAIL_USE_TLS = external_settings.EMAIL_USE_TLS
EMAIL_HOST_USER = external_settings.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
PUBLIC_ID_LENGTH = external_settings.PUBLIC_ID_LENGTH

FIREBASE_CREDENTIALS_PATH = external_settings.FIREBASE_CREDENTIALS_PATH


# initialize firebase
FIREBASE_CREDENTIALS = firebase_admin.credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
default_app = firebase_admin.initialize_app(FIREBASE_CREDENTIALS)
