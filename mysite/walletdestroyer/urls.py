from django.urls import path
from .views import SpendingView, EarningsView, test_view, RegisterUserView, logout_view, AuthUserView, StartView

urlpatterns = [
    path('earnings/', EarningsView.as_view(), name='earnings'),
    path('spending/', SpendingView.as_view(), name='spending'),
    path('registration/', RegisterUserView.as_view(), name='registration'),
    path('auth/', AuthUserView.as_view(), name='auth'),
    path('logout/', logout_view, name='logout'),
    path('', StartView.as_view(), name='start_page')
]
