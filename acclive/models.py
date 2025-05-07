from django.db import models
from django.utils.timezone import now
from decimal import Decimal

class TableEntry(models.Model):
    date = models.DateField(default=now)
    site_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    bank = models.BooleanField(default=False)  # Checkbox for bank transaction
    income = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    expense = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, editable=False)
    transaction_type = models.CharField(
        max_length=20, choices=[("Withdrawal", "Withdrawal"), ("Transfer", "Transfer"), ("Deposit", "Deposit")],
        blank=True, null=True
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    amount_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, editable=False)
    check_number = models.CharField(max_length=50, blank=True, default="")
    deleted = models.BooleanField(default=False)  # Soft delete field

    def save(self, *args, **kwargs):
        try:
            # Get previous entries, excluding deleted ones
            previous_entries = TableEntry.objects.filter(date__lt=self.date, deleted=False).order_by('-date')
            previous_non_bank_entry = previous_entries.filter(bank=False).first()
            previous_bank_entry = previous_entries.filter(bank=True).first()

            # Calculate balances using Decimal for precision
            previous_balance = Decimal(str(previous_non_bank_entry.balance if previous_non_bank_entry else '0'))
            previous_amount_balance = Decimal(str(previous_bank_entry.amount_balance if previous_bank_entry else '0'))

            # Ensure income and expense are Decimal
            self.income = Decimal(str(self.income))
            self.expense = Decimal(str(self.expense))
            self.amount = Decimal(str(self.amount))

            # Calculate new balance
            self.balance = previous_balance + self.income - self.expense
            self.amount_balance = previous_amount_balance

            # Update amount_balance for bank transactions
            if self.bank:
                if self.transaction_type in ["Withdrawal", "Transfer"]:
                    self.amount_balance -= self.amount
                elif self.transaction_type == "Deposit":
                    self.amount_balance += self.amount

            # Ensure check_number is never None
            if self.check_number is None:
                self.check_number = ""

            super().save(*args, **kwargs)

            # Update subsequent entries' balances
            self._update_subsequent_entries()

        except Exception as e:
            raise ValueError(f"Error saving entry: {str(e)}")

    def _update_subsequent_entries(self):
        """Update balances for all entries after this one."""
        subsequent_entries = TableEntry.objects.filter(
            date__gt=self.date,
            deleted=False
        ).order_by('date')

        current_balance = self.balance
        current_amount_balance = self.amount_balance

        for entry in subsequent_entries:
            entry.balance = current_balance + entry.income - entry.expense
            
            if entry.bank:
                if entry.transaction_type in ["Withdrawal", "Transfer"]:
                    entry.amount_balance = current_amount_balance - entry.amount
                elif entry.transaction_type == "Deposit":
                    entry.amount_balance = current_amount_balance + entry.amount
                current_amount_balance = entry.amount_balance
            
            current_balance = entry.balance
            entry.save(update_fields=['balance', 'amount_balance'])

    def __str__(self):
        return f"{self.date} - {self.site_name} - Balance: {self.balance}"