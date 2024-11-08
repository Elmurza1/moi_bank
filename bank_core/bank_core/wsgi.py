import os
import sys
from django.core.wsgi import get_wsgi_application

# Добавьте путь к корневой директории проекта
sys.path.append('/home/MoiBank')  # Путь к директории проекта
sys.path.append('/home/Moibank/bank_core')  # Путь к директории с модулем bank_core

# Укажите настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank_core.settings')

application = get_wsgi_application()
