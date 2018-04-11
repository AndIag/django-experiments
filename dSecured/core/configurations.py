from core import credentials

DEBUG = True
FORCE_SSL = True

SECRET_KEY = credentials.SECRET_KEY
ALLOWED_HOSTS = []
CORS_WHITELIST = ['google.com']

DB_CREDENTIALS = credentials.DB_CREDENTIALS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': DB_CREDENTIALS.get("DATABASE_USERNAME", None),
        'PASSWORD': DB_CREDENTIALS.get("DATABASE_PASSWORD", None),
        'HOST': 'localhost',
        'PORT': '5432'
    },
    'OPTIONS': {
        'client_encoding': 'UTF8',
        'timezone': 'UTC'
    }
}
