from django.db import models

# Create your models here.


class Interpreter(models.Model):

    type = models.ForeignKey(
        "transactions.Transaction",
        on_delete=models.CASCADE,
        related_name='transactions'
    )
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.DateTimeField()
    store_own = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
