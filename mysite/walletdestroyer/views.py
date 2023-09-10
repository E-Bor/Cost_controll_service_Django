from django.http import HttpResponse
from django.shortcuts import render
from django.urls import resolve
from django.views import View

from .db_writer import DbManager, writer
from .forms import EarningsForm, SpendingForm


# from mysite.walletdestroyer.forms import EarningsForm


# Create your views here.


class EarningsView(View):

    params = {
        'operations': [
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
        ],
        'form': EarningsForm()
    }

    def get(self, request):

        a = request.path_info
        b = resolve(a)

        # return render(request, 'walletdestroyer/base.html')
        return render(request, 'walletdestroyer/earnings.html', context=self.params)

    def post(self, request):
        print(request.POST)
        data = {'money': 4, 'description': 'qewr'}
        writer.create(data)
        a = writer.get_latest()
        print(a)
        return render(request, 'walletdestroyer/earnings.html', context=self.params)

    # @property
    # def earning_form(self):
    #     return EarningsForm()


class SpendingView(View):

    # TODO: refactor to dataclasses

    params = {
        'operations': [
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
        ],
        'form': SpendingForm(),
        'categories': ['cat1', 'cat2', 'cat3', 'cat4']
    }

    def get(self, request):
         return render(request, 'walletdestroyer/spending.html', context=self.params)

    def post(self, request):
        print(request.POST)
        return render(request, 'walletdestroyer/spending.html', context=self.params)

