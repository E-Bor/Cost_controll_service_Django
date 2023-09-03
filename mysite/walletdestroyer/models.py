from django.db import models

# Create your models here.


class MoneyTransactionModel(models.Model):
    money = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    transaction_type = models.ForeignKey('TransactionTypesModel', on_delete=models.CASCADE, null=True)


class TransactionTypesModel(models.Model):
    type_name = models.CharField(max_length=10)
