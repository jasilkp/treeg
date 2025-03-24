from django import forms
from .models import BankAccount

class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ['name', 'balance']

