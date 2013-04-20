# DEVELOPMENT SPECIFIC SETTINGS GOES HERE
from pytraining.settings import *


DEBUG = TEMPLATE_DEBUG = True


ALLOWED_HOSTS = ('127.0.0.1', )


INSTALLED_APPS.extend([
    'django_extensions',
    #'debug_toolbar',
])


#MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
