from django.db import models
from django.contrib.auth.models import User

class Ombor(models.Model):
    ism = models.CharField(max_length=50)
    dokon_nomi = models.CharField(max_length=150)
    tel = models.CharField(max_length=20)
    manzil = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.ism} ({self.dokon_nomi})"
