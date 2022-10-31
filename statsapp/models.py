from django.db import models
from asosiyapp.models import *

class Stats(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)
    sana = models.DateField()
    miqdor = models.PositiveIntegerField()
    summa = models.BigIntegerField()
    tolandi = models.BigIntegerField()
    nasiya = models.BigIntegerField()

    def __str__(self):
        return f"{self.ombor} ({self.client} {self.product})"

