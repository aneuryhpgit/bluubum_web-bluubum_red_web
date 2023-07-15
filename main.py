import os
import sys
from django.core.wsgi import get_wsgi_application

# Agrega el directorio raíz del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Establece la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Obtén la aplicación WSGI de Django
application = get_wsgi_application()
