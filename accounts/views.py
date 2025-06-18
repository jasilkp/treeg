from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save immediately
            user.is_staff = True  # Mark as accountant
            user.save()  # Save after setting is_staff
            login(request, user)  # Log the user in after registration
            return redirect('dashboard')  # Redirect to dashboard
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def create_superuser_temp(request):
    """Temporary view to create superuser - REMOVE AFTER USE"""
    User = get_user_model()
    username = 'admin'
    email = 'admin@example.com'
    password = '1234'
    
    try:
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.is_active = True
            user.save()
            return HttpResponse(f"Updated existing user '{username}' with password '{password}'")
        else:
            user = User.objects.create_superuser(username, email, password)
            return HttpResponse(f"Created new superuser '{username}' with password '{password}'")
    except Exception as e:
        return HttpResponse(f"Error: {e}")


