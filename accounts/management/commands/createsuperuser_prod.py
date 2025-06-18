from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection

class Command(BaseCommand):
    help = 'Create or update a superuser for production'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        # Check if database is connected
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            self.stdout.write(self.style.SUCCESS('Database connection successful'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Database connection failed: {e}'))
            return
        
        # Check if User table exists
        try:
            user_count = User.objects.count()
            self.stdout.write(self.style.SUCCESS(f'User table exists. Total users: {user_count}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'User table error: {e}'))
            return
        
        username = 'admin'
        email = 'admin@example.com'
        password = '1234'
        
        try:
            if User.objects.filter(username=username).exists():
                # User exists, update password and permissions
                user = User.objects.get(username=username)
                user.set_password(password)
                user.is_superuser = True
                user.is_staff = True
                user.is_active = True
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Updated existing user "{username}" with new password'))
            else:
                # Create new superuser
                user = User.objects.create_superuser(username, email, password)
                self.stdout.write(self.style.SUCCESS(f'Created new superuser "{username}"'))
            
            # Verify the user was created/updated correctly
            user = User.objects.get(username=username)
            if user.check_password(password):
                self.stdout.write(self.style.SUCCESS(f'Password verification successful for "{username}"'))
            else:
                self.stdout.write(self.style.ERROR(f'Password verification failed for "{username}"'))
                
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating/updating user: {e}')) 