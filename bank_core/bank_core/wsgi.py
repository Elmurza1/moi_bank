import os

from django.core.wsgi import get_wsgi_application


# Укажите настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank_core.settings')

application = get_wsgi_application()
