from rest_framework import routers

from .views import SpendingViewSet

spending_router = routers.DefaultRouter()
spending_router.register(r'spending', SpendingViewSet)
