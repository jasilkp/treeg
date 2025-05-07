from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from .forms import ClientForm
from .models import Client


@login_required
def add_client(request):
    if request.method == "POST":
        form = ClientForm ( request.POST )
        if form.is_valid ():
            form.save ()
            return redirect ( 'dashboard' )
    else:
        form = ClientForm ()

    return render ( request , 'add_client.html' , {'form': form} )

@login_required
def delete_client(request, client_id):
    if request.method == 'POST':
        client = get_object_or_404(Client, id=client_id)
        client.deleted = True
        client.deleted_at = timezone.now()
        client.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

