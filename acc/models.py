from django.db import models
from django.utils.timezone import now

class TableEntry(models.Model):
    date = models.DateField(default=now)
    site_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    income = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    expense = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Get the most recent entry before this one
        previous_entry = TableEntry.objects.filter(date__lt=self.date).order_by('-date').first()
        previous_balance = previous_entry.balance if previous_entry else 0

        # Calculate new balance
        self.balance = previous_balance + self.income - self.expense
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} - {self.site_name} - Balance: {self.balance}"
