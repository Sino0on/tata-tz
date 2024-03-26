import os
from datetime import timedelta
from pathlib import Path
from django.utils.translation import gettext_lazy as _
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY", default="django-insecure-#++s##2(v-25y73$k7uu)4j&3og19ci-t4=p1f1en03#-e*@dq")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ['*']

# CSRF_TRUSTED_ORIGINS = ['https://']

# Application definition


PROJECT_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DJANGO_APPS = [
    'apps.authentication',
    'apps.restaurant',
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "django_filters",
    "corsheaders",
    "drf_spectacular",
]

INSTALLED_APPS = [*DJANGO_APPS, *THIRD_PARTY_APPS, *PROJECT_APPS]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'


TEMPLATE_DIR = os.path.join(BASE_DIR, "apps/templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config("PG_NAME", default="tata_dev"),
        'USER': config("PG_USER", default="tata_user"),
        'PASSWORD': config("PG_PASS", default="qwerty2003"),
        'HOST': config("PG_HOST", default="db"),
        'PORT': config("PG_PORT", default="5432"),
    }
}


CORS_ALLOW_ALL_ORIGINS = True


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(BASE_DIR, "apps/static"),)

MEDIA_ROOT = os.path.join(BASE_DIR, "apps/media")
MEDIA_URL = "/media/"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser'
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_THROTTLE_RATES": {
        "auth": '3/min',
    }
}

if DEBUG:
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"].append("rest_framework.authentication.BasicAuthentication")

# OpenAPI settings

SPECTACULAR_SETTINGS = {
    "TITLE": "Tata tz",
    "DESCRIPTION": "Описание нашего API в разработке...",
    'COMPONENT_SPLIT_REQUEST': True,
    "VERSION": "1.0.0",
    "SCHEMA_PATH_PREFIX": r"/api/v[0-9]",
    "SERVE_PERMISSIONS": ("rest_framework.permissions.IsAdminUser", ),
    "SERVE_AUTHENTICATION": ('rest_framework.authentication.SessionAuthentication',
                             'rest_framework.authentication.BasicAuthentication'),
    "PREPROCESSING_HOOKS": ("api.openapi.preprocessors.get_urls_preprocessor",),
    "SWAGGER_UI_SETTINGS": {
        "docExpansion": "none",  # 'none' | 'list' | 'full'
    },
    "ENUM_NAME_OVERRIDES": {
        "RatingsEnum": "apps.autoanswers.models.RatingChoices",
        "CountMonthsEnum": "api.billing.serializers.PeriodChoices",
    },
    "SERVE_PERMISSIONS": ("rest_framework.permissions.AllowAny",)
}


SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "UPDATE_LAST_LOGIN": True,
    "ROTATE_REFRESH_TOKENS": True,
}
