from django.db import models
from django.forms import model_to_dict


# Create your models here.

class SpendingCategoriesModel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_categories():
        return SpendingCategoriesModel.objects.all().values_list('name', 'name')

class SpendingModel(models.Model):
    user_id = models.PositiveIntegerField()
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
        verbose_name = 'Spending'
        verbose_name_plural = 'Spending'
        ordering = ['-time_create']

    def to_dict(self):
        data = model_to_dict(self)
        data['category'] = self.category.name if self.category else None
        return data


class EarningModel(models.Model):
    user_id = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()
    time_create = models.DateField()

    class Meta:
        verbose_name = 'Earning'
        ordering = ['-time_create']

    def to_dict(self):
        return model_to_dict(self)
