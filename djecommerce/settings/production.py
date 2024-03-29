from .base import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('d3u85pr3rhajlb'),
        'USER': config('egviqwdcbgawxg'),
        'PASSWORD': config('47ec3907b02e0a1ecbe609f41cfb923cf4920206f27cc0dd727dc75790e965ff'),
        'HOST': config('ec2-3-91-139-25.compute-1.amazonaws.com'),
        'PORT': ''
    }
}




db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')