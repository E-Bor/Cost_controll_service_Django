from django.urls import path
from .views import SpendingView, EarningsView

urlpatterns = [
    path('earnings/', EarningsView.as_view(), name='earnings'),
    path('spending/', SpendingView.as_view(), name='spending'),
]
