import os
from pathlib import Path

import cloudinary
from django.conf.global_settings import AUTH_PASSWORD_VALIDATORS

from french_bulldog_store.utils import is_production, is_test

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.getenv('DEBUG', 'False') == 'True'
APP_ENVIRONMENT = os.getenv('APP_ENVIRONMENT', 'Development')
SECRET_KEY = os.getenv('SECRET_KEY', 'sk')

ALLOWED_HOSTS = [
    'french-bulldog-store.herokuapp.com',
    '127.0.0.1'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',

    'french_bulldog_store.auth_app',
    'french_bulldog_store.cart',
    'french_bulldog_store.web',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'french_bulldog_store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'french_bulldog_store.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd8jqv3hiprqitd',
        'USER': 'xhhbudiadgagiw',
        'PASSWORD': '9345a8b223dbe9fc6010fae315259fd31a9ddeef778d934fcc01f1700cbfbbe7',
        'HOST': 'ec2-34-242-84-130.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}

if is_production():
    AUTH_PASSWORD_VALIDATORS.extend([
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
    ])

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR, '../static/images')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = 'home page'

LOGGING_LEVEL = 'DEBUG'

if is_production():
    LOGGING_LEVEL = 'INFO'
elif is_test():
    LOGGING_LEVEL = 'CRITICAL'

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'level': LOGGING_LEVEL,
            'filters': [],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': LOGGING_LEVEL,
            'handlers': ['console'],
        }
    }
}

AUTH_USER_MODEL = 'auth_app.FrenchieUser'

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME', None),
    api_key=os.getenv('CLOUDINARY_API_KEY', None),
    api_secret=os.getenv('CLOUDINARY_API_SECRET', None),
)