from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .forms import ClientForm


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

