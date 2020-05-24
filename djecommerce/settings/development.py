import dj_database_url

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ty-one.herokuapp.com', '127.0.0.1']

INSTALLED_APPS += [
   'debug_toolbar'
]

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

# DEBUG TOOLBAR SETTINGS

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        #'NAME': os.path.join(BASE_DIR, 'tylersdatabase_one'),
        'NAME': os.path.join('d3u85pr3rhajlb'),
        'USER': 'egviqwdcbgawxg',
        'PASSWORD': '47ec3907b02e0a1ecbe609f41cfb923cf4920206f27cc0dd727dc75790e965ff',
        'HOST': 'ec2-3-91-139-25.compute-1.amazonaws.com',
        'PORT': '5432',


    }
}


STRIPE_PUBLIC_KEY = ''
STRIPE_SECRET_KEY = ''
