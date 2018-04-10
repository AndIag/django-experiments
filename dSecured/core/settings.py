import os

from core import configurations

ROOT_URLCONF = 'core.urls'
SECRET_KEY = configurations.SECRET_KEY
DEBUG = configurations.DEBUG

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
LOG_DIR = os.path.join(BASE_DIR, 'core', 'logs')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

ALLOWED_HOSTS = configurations.ALLOWED_HOSTS

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = configurations.DB_CREDENTIALS

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# CORS configuration
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = ALLOWED_HOSTS + configurations.CORS_WHITELIST
CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS
if DEBUG:  # If we are debugging include Django host and Angular2 host
    CORS_ORIGIN_WHITELIST.append('localhost:8080')
    CORS_ORIGIN_WHITELIST.append('localhost:4200')
CORS_ALLOW_METHODS = ('DELETE', 'GET', 'POST', 'PUT', 'OPTIONS')
CORS_ALLOW_HEADERS = ('accept', 'authorization', 'content-type')

# SSL configuration
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
    'admin_honeypot',
    'corsheaders',
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
