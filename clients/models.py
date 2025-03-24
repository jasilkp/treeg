from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    amount_given = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
