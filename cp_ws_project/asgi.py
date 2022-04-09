"""
ASGI config for cp_ws_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from cp_ws_project.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cp_ws_project.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': URLRouter(ws_urlpatterns)
    }
)
