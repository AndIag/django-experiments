import os

from core import configurations

ROOT_URLCONF = 'core.urls'
SECRET_KEY = configurations.SECRET_KEY
DEBUG = configurations.DEBUG

WSGI_APPLICATION = 'core.wsgi.application'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
LOG_DIR = os.path.join(BASE_DIR, 'core', 'logs')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

DATABASES = configurations.DATABASES

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# CORS configuration
# Control Cross-Origin-Resource-Sharing to allow access to our service from other sites, it's value depends on
# DEBUG and ALLOWED_HOSTS configurations and can be complemented using CORS_WHITELIST setting in configurations.py.
#
# If DEBUG is set to True allow all origins enabling access to the site for everywhere, also, add localhost connections
# to WHITELIST from 8080 and 4200 ports.
#
# By default whitelist is set as ALLOWED_HOSTS + CORS_WHITELIST
ALLOWED_HOSTS = configurations.ALLOWED_HOSTS
CORS_ORIGIN_ALLOW_ALL = DEBUG
if not DEBUG:
    CORS_ORIGIN_WHITELIST = ALLOWED_HOSTS + configurations.CORS_WHITELIST
    CORS_ALLOW_METHODS = ('DELETE', 'GET', 'POST', 'PUT', 'OPTIONS')
    CORS_ALLOW_HEADERS = ('accept', 'authorization', 'content-type', 'accept-language')
CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS

# SSL configuration
# If FORCE_SSL is set to True in configurations.py hard force the use of SSL in all the connections.
if configurations.FORCE_SSL:
    # Force SSL in all requests
    SECURE_SSL_REDIRECT = True
    SECURE_REDIRECT_EXEMPT = []
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # Force HSTS header
    # https://docs.djangoproject.com/en/2.0/ref/middleware/#http-strict-transport-security
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'admin_honeypot',
    'corsheaders',
    'oauth2_provider',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',  # Required if CORS and CRSF are enabled
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(STATIC_ROOT, 'templates')],
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

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 4
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 30,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'ORDERING_PARAM': 'sort',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
        'rest_framework.throttling.ScopedRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/minute',
        'user': '1000/day'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file_all': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'filename': os.path.join(LOG_DIR, 'django_debug.log'),
            'formatter': 'verbose',
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'filename': os.path.join(LOG_DIR, 'django_errors.log'),
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'include_html': True,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'core.custom': {
            'handlers': ['console', 'file', 'file_all', 'mail_admins'],
            'level': 'DEBUG',
        }
    }
}
