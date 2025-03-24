from django.shortcuts import render, redirect
from django.contrib.auth import login
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


