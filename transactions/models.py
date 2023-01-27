from django.db import models

# Create your models here.


class Transaction(models.Model):
    type = models.IntegerField(unique=True)
    description = models.CharField(max_length=255, unique=True)
    nature = models.CharField(max_length=255)
    sinal = models.CharField(max_length=255)
