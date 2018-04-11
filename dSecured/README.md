# Security Settings
    - FORCE_SSL
Configure all required settings to force SSL, HTTPS and HSTS connections.

    - CORS settings
Control Cross-Origin-Resource-Sharing to allow access to our service from other sites, it's value depends on
DEBUG and ALLOWED_HOSTS configurations and can be complemented using CORS_WHITELIST setting in configurations.py.

If DEBUG is set to True allow all origins enabling access to the site for everywhere, also, add localhost connections
to WHITELIST from 8080 and 4200 ports.

By default whitelist is set as ALLOWED_HOSTS + CORS_WHITELIST.

# Configurations

```yaml
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
```
