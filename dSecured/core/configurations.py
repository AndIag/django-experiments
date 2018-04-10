from core import credentials

DEBUG = True
FORCE_SSL = True

SECRET_KEY = credentials.SECRET_KEY
ALLOWED_HOSTS = []
CORS_WHITELIST = ['google.com']

DB_CREDENTIALS = credentials.DB_CREDENTIALS
