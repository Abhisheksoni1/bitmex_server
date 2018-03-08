"""
WSGI config for bitmex_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bitmex_server.settings")

application = get_wsgi_application()

application = WhiteNoise(application, root='static')
application.add_files('staticfiles', prefix='more-files/')