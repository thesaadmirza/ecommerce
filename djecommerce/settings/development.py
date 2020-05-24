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
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': os.path.join(BASE_DIR, 'tylersdatabase_one'),
        'NAME': os.path.join('tylersdatabase_one'),
        'USER': 'mcadmin',
        'PASSWORD': 'lollypop33',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },

    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

STRIPE_PUBLIC_KEY = ''
STRIPE_SECRET_KEY = ''
