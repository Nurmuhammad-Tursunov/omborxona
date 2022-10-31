from django.db import models
from userapp.models import *

class Product(models.Model):
    nomi = models.CharField(max_length=200)
    brend = models.CharField(max_length=200)
    miqdor = models.IntegerField()
    kelgan_narx = models.BigIntegerField()
    sotuv_narx = models.BigIntegerField()
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nomi} ({self.brend})"


class Client(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    dokon = models.CharField(max_length=50)
    manzil = models.CharField(max_length=200)
    qarz = models.IntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ism} ({self.dokon})"
