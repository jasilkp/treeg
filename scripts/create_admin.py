import os
import sys
# Ensure project root is on sys.path so we can import `accounting` when this
# script is executed from the `scripts/` directory.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accounting.settings')
import django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin'
password = '1234'
email = 'admin@example.com'

try:
    user = User.objects.filter(username=username).first()
    if user:
        user.is_staff = True
        user.is_superuser = True
        user.email = email
        user.set_password(password)
        user.save()
        print("Updated existing user 'admin' and set password.")
    else:
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Created superuser 'admin'.")
except Exception as e:
    import traceback
    print('Failed to create/update user:', e)
    traceback.print_exc()
