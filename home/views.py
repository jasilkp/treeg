from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from clients.models import Client
from transactions.models import Transaction
from bank.models import BankAccount
from django.db.models import Sum




from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def dashboard(request):
    if not request.user.is_authenticated:  # Redirect to login if not logged in
        return redirect('login')

    clients = Client.objects.all().order_by('-id')
    bank_accounts = BankAccount.objects.all()

    # Calculate total bank balance
    total_bank_balance = sum(account.balance for account in bank_accounts)

    context = {
        'clients': clients,
        'bank_accounts': bank_accounts,
        'total_bank_balance': total_bank_balance,
    }

    return render(request, 'home/dashboard.html', context)

@login_required
def client_details(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    transactions = Transaction.objects.filter(client=client).order_by('-id')

    # Calculate total sum of transactions
    total_amount = transactions.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'client': client,
        'transactions': transactions,
        'total_amount': total_amount,
    }

    return render(request, 'home/client_details.html', context)



@login_required
def delete_client(request , client_id):
    client = get_object_or_404 ( Client , id=client_id )
    client.delete ()
    return redirect ( 'dashboard' )

