from django.db import models

# Create your models here.
from django.db import models

class BankAccount(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
