from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import resolve, reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .models import EarningModel, SpendingModel, SpendingCategoriesModel
from .db_writer import DbManager
from .forms import EarningsForm, SpendingForm, UserRegisterForm, AuthUserForm


# from mysite.walletdestroyer.forms import EarningsForm


# Create your views here.


class StartView(View):

    # TODO: create startpage, which will redirect user to auth page
    def get(self, request):
        return HttpResponse('startpage')



class EarningsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('auth')

    Writer = DbManager(EarningModel)

    def get(self, request):
        params = {
            'operations': self.Writer.get_latest(view_depth=5),
            'form': EarningsForm(),
            'table_name': EarningModel._meta.verbose_name,
            'is_auth': request.user.is_authenticated
        }
        return render(request, 'walletdestroyer/earnings.html', context=params)

    def post(self, request):

        self.Writer.create(request.POST)

        return redirect('earnings', permanent=True)


class SpendingView(LoginRequiredMixin, View):
    Writer = DbManager(SpendingModel)
    login_url = reverse_lazy('auth')

    SPENDING_CATEGORIES = SpendingCategoriesModel.objects.all()

    def get(self, request):

        params = {
            'operations': self.Writer.get_latest(view_depth=5),
            'form': SpendingForm(),
            'table_name': SpendingModel._meta.verbose_name,
            'categories': self.SPENDING_CATEGORIES,
            'is_auth': request.user.is_authenticated
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


class RegisterUserView(CreateView):
    form_class = UserRegisterForm
    template_name = 'walletdestroyer/reg.html'
    success_url = reverse_lazy('spending')


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('spending')
# qQ1234Qqqrr

class AuthUserView(LoginView):
    form_class = AuthUserForm
    template_name = 'walletdestroyer/auth.html'

    def get_success_url(self):
        return reverse_lazy('spending')

def test_view(request):
    return HttpResponse('hello')


def logout_view(request):
    logout(request)
    return redirect('auth')
