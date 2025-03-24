from django.db import models
from django.utils import timezone  # Import timezone for default value
from clients.models import Client

class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)  # Allows manual date input

    def __str__(self):
        return f"{self.client.name} - {self.amount} on {self.date}"


