from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm
from clients.models import Client
from django.http import JsonResponse


@login_required
def add_transaction(request , client_id):
    client = get_object_or_404 ( Client , id=client_id )

    if request.method == "POST":
        form = TransactionForm ( request.POST )
        if form.is_valid ():
            transaction = form.save ( commit=False )
            transaction.client = client  # Assign transaction to the client
            transaction.save ()
            return redirect ( 'client_details' , client_id=client.id )  # Redirect back to client details
    else:
        form = TransactionForm ()

    # Retrieve all transactions for the selected client
    transactions = Transaction.objects.filter ( client=client )

    # Calculate the Grand Total of transactions for this client
    total_amount = sum ( transaction.amount for transaction in transactions )

    return render ( request , 'add_transaction.html' , {
        'form': form ,
        'client': client ,
        'transactions': transactions ,
        'total_amount': total_amount  # Pass Grand Total to template
    } )


@login_required
def delete_transaction(request, transaction_id):
    if request.method == 'POST':
        transaction = get_object_or_404(Transaction, id=transaction_id)
        client_id = transaction.client.id
        transaction.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

