import os

import dj_database_url

from pytraining.settings import *


ADMINS = (
     ('Ilian Iliev', 'ilian@i-n-i.org'),
)


# PRODUCTION SPECIFIC SETTINGS GOES HERE
DEBUG = TEMPLATE_DEBUG = False

DATABASES = {'default': dj_database_url.config()}


EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME', None)
EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD', None)


ALLOWED_HOSTS = ('floating-basin-9649.herokuapp.com',
                 'www.pytraining.net')
