from django.urls import path, include

from .routers import spending_router
from .views import ReferencesAPIView, EarningListAPIView, EarningCRUDAPIView

urlpatterns = [
    path('references/', ReferencesAPIView.as_view()),
    path('earnings/', EarningListAPIView.as_view()),
    path('earnings/<int:pk>', EarningCRUDAPIView.as_view()),
    path('', include(spending_router.urls))
]
