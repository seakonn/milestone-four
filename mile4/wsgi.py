import os
from django.core.wsgi import get_wsgi_application

"""
********************************************************************

ORIGINAL CODE IN THIS FILE COPIED FROM:

https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation/tree/master/07-CustomAuthentication/01-email_authentication/django_auth

********************************************************************
"""

"""
WSGI config for mile4 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mile4.settings")

application = get_wsgi_application()
