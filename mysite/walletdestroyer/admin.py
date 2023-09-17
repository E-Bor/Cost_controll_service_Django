from django.contrib import admin
from .models import (
    SpendingCategoriesModel,
    SpendingModel,
    EarningModel
)

# Register your models here.

class SpendingAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'cost', 'time_create', 'category', 'description')
    list_display_links = ('user_id',)
    search_fields = ('user_id',)

class EarningAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'cost', 'time_create')
    list_display_links = ('user_id',)
    search_fields = ('user_id',)

class SpendingCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)


admin.site.register(SpendingCategoriesModel, SpendingCategoriesAdmin)
admin.site.register(SpendingModel, SpendingAdmin)
admin.site.register(EarningModel, EarningAdmin)
