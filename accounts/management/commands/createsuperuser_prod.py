from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create or update a superuser for production'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', '1234')
            self.stdout.write(self.style.SUCCESS('Superuser created!'))
        else:
            user = User.objects.get(username='admin')
            user.set_password('1234')
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.WARNING('Superuser already existed, password reset!')) 