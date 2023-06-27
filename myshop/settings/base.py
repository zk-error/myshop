import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent



SECRET_KEY = 'egnobnwi-nsedjacruhite-+2@@zj&oz^i(fj%j%k8sw#5q_h%1i9tjtl)kzh!ormqedaibmq'

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #appss nativas
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'cuentas.apps.CuentasConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',

    #apps externas
    'social_django',
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

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static',]
# STATIC_ROOT = BASE_DIR / 'static'



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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True





MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

#session id 
CART_SESSION_ID = 'cart'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#redireccion
LOGIN_REDIRECT_URL = "shop:product_list"
LOGOUT_REDIRECT_URL = "shop:product_list"
#esta es la ruta que debe segir un usuario no aunteticodo cuando usamos el decorador @login_required por ejemplo
LOGIN_URL = "cuentas:login"

#modelo personalizado y autentificacion
AUTH_USER_MODEL = 'cuentas.User'
AUTHENTICATION_BACKENDS = [
    'cuentas.auth.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
]

#autentificacion con google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '590621193871-0o0ne91je2p67s2j06pev4baobnr6te0.apps.googleusercontent.com' # Google Client ID
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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' # Google Client Secret

#email consola
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#para hacer la conexcion con el contenedor
# CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'
CELERY_BROKER_URL = 'amqp://dani:holabb@rabbitmq:5672//'

# Stripe settings
STRIPE_PUBLISHABLE_KEY = 'pk_test_51Moh57Bk1Tg0smHHMg3TA000YuihdVGwh525smRo9fIX3qD07cXcsm15O0nG1QO2XMxGixaunSKbilpBRWNrgeGB00nCQVC8NQ' # Publishable key
STRIPE_SECRET_KEY = 'sk_test_51Moh57Bk1Tg0smHHKsNnFOueWtO0e0wKUinU5QaioshIqwwbjFbYgaNVwvBCtW46AwHijETAbzEVKUB858foncAE00qV5jAOos' # Secret key
STRIPE_API_VERSION = '2022-08-01'

#para webhook
STRIPE_WEBHOOK_SECRET = 'whsec_6e60d6a21d257623bcf368664826b8a1cda70e323da6589950e002706e5eb6f8'

# Redis settings
# REDIS_HOST = 'localhost'
REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 1

# Email server configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'magyholabbchacal2002@gmail.com'
EMAIL_HOST_PASSWORD = 'ezlvssldmilbsrtg'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

