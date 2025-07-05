"""
WSGI configuration for accounting project on PythonAnywhere.
"""

import os
import sys

# Add your project directory to the sys.path
path = '/home/Ableaccounting/accounting'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'accounting.settings'

# Import Django's WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 