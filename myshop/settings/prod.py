import os
from .base import *
DEBUG = False

ADMINS = [
    ('Antonio M', 'email@mydomain.com'),
]
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get('POSTGRES_DB'),
    'USER': os.environ.get('POSTGRES_USER'),
    'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
    'HOST': 'db',
    'PORT': 5432,
    }
}

# Security SSL/TLS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
