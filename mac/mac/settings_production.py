from .settings import *  # noqa

import os

DEBUG = False

ALLOWED_HOSTS = ["makers-against-c.com"]

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600

SECRET_KEY = os.environ.get("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django_prometheus.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DB_NAME'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'HOST': os.environ.get('MYSQL_HOST'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'connect_timeout': 1,
        },
    },
}
