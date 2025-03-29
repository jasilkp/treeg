from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now


class TableEntry ( models.Model ):
    date = models.DateField ( default=now )
    site_name = models.CharField ( max_length=255 )
    description = models.TextField ( blank=True , null=True )
    bank = models.BooleanField ( default=False )  # Checkbox for bank transaction
    income = models.DecimalField ( max_digits=15 , decimal_places=2 , default=0.00 )
    expense = models.DecimalField ( max_digits=15 , decimal_places=2 , default=0.00 )
    balance = models.DecimalField ( max_digits=15 , decimal_places=2 , default=0.00 , editable=False )
    transaction_type = models.CharField (
        max_length=20 , choices=[("Withdrawal" , "Withdrawal") , ("Transfer" , "Transfer") , ("Deposit" , "Deposit")] ,
        blank=True , null=True
    )
    amount = models.DecimalField ( max_digits=15 , decimal_places=2 , default=0.00 )
    amount_balance = models.DecimalField ( max_digits=15 , decimal_places=2 , default=0.00 , editable=False )
    check_number = models.CharField ( max_length=50 , blank=True , null=True )
    deleted = models.BooleanField ( default=False )  # Soft delete field

    def save(self , *args , **kwargs):
        previous_entry = TableEntry.objects.filter ( date__lt=self.date , deleted=False ).order_by ( '-date' ).first ()
        previous_balance = previous_entry.balance if previous_entry else 0
        self.balance = previous_balance + self.income - self.expense
        self.amount_balance = self.balance if self.bank else 0
        super ().save ( *args , **kwargs )

    def __str__(self):
        return f"{self.date} - {self.site_name} - Balance: {self.balance}"
