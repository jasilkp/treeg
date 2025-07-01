import sys
import os

# Add your project directory to the sys.path
project_home = '/home/Ableaccounting/accounting'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'accounting.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 