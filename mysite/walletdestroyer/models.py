import datetime

from django.db import models

# Create your models here.

class SpendingCategoriesModel(models.Model):
    name = models.CharField(max_length=30)

class SpendingModel(models.Model):
    cost = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    time_create = models.DateField()
    time_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        'SpendingCategoriesModel',
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        verbose_name = 'Траты'
        ordering = ['time_create']


class EarningModel(models.Model):
    cost = models.PositiveIntegerField()
    time_create = models.DateField()

    class Meta:
        verbose_name = 'Заработок'
        ordering = ['time_create']