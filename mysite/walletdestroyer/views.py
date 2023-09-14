from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import resolve
from django.views import View

from .models import EarningModel, SpendingModel, SpendingCategoriesModel
from .db_writer import DbManager
from .forms import EarningsForm, SpendingForm


# from mysite.walletdestroyer.forms import EarningsForm


# Create your views here.


class EarningsView(View):

    Writer = DbManager(EarningModel)

    def get(self, request):
        params = {
            'operations': self.Writer.get_latest(view_depth=5),
            'form': EarningsForm(),
            'table_name': EarningModel._meta.verbose_name
        }
        return render(request, 'walletdestroyer/earnings.html', context=params)

    def post(self, request):

        self.Writer.create(request.POST)

        return redirect('earnings', permanent=True)


class SpendingView(View):
    Writer = DbManager(SpendingModel)

    SPENDING_CATEGORIES = SpendingCategoriesModel.objects.all()

    def get(self, request):

        params = {
            'operations': self.Writer.get_latest(view_depth=5),
            'form': SpendingForm(),
            'table_name': SpendingModel._meta.verbose_name,
            'categories': self.SPENDING_CATEGORIES
        }
        return render(request, 'walletdestroyer/spending.html', context=params)

    def post(self, request):
        data = request.POST.copy()
        if data.get('category') == 'Выберите':
            data['category'] = self.SPENDING_CATEGORIES[0]
        for category in self.SPENDING_CATEGORIES:
            if data.get('category') == category.name:
                data['category'] = category

        self.Writer.create(data)

        return redirect('spending', permanent=True)

