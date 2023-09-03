from django.http import HttpResponse
from django.shortcuts import render
from django.urls import resolve
from django.views import View


# Create your views here.


class EarningsView(View):

    def get(self, request):
        params = {'operations': [
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'odezhda', 'date': '14-10-2023'},
        ]}
        a = request.path_info
        b = resolve(a)

        # return render(request, 'walletdestroyer/base.html')
        return render(request, 'walletdestroyer/earnings.html', context=params)


class SpendingView(View):

    def get(self, request):
        params = {'operations': [
            {'cost': 123, 'category': 'eda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'eda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'eda', 'date': '14-10-2023'},
            {'cost': 123, 'category': 'eda', 'date': '14-10-2023'},
        ]}
        return render(request, 'walletdestroyer/spending.html', context=params)
