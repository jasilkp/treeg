from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Date Picker

    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'date']

