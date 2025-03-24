from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BankAccount
from .forms import BankAccountForm

@login_required
def add_bank_account(request):
    if request.method == "POST":
        form = BankAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank_account_list')  # Redirect to the bank account list
    else:
        form = BankAccountForm()
    return render(request, 'add_bank_account.html', {'form': form})

@login_required
def bank_account_list(request):
    bank_accounts = BankAccount.objects.all()
    return render(request, 'bank_account_list.html', {'bank_accounts': bank_accounts})

