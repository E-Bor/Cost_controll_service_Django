from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SpendingSerializer, EarningSerializer
from walletdestroyer.models import SpendingModel, EarningModel

# Create your views here.

class ReferencesAPIView(APIView):

    BASE_URL = 'api/v1/'
    ENDPOINTS_MAP = (
        f'{BASE_URL}references',
    )

    def get(self, request):
        return Response(self.ENDPOINTS_MAP)


class SpendingViewSet(viewsets.ModelViewSet):
    queryset = SpendingModel.objects.all()
    serializer_class = SpendingSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        if user_id:
            queryset = SpendingModel.objects.filter(user_id=user_id)
            return queryset


class EarningListAPIView(generics.ListAPIView):
    queryset = EarningModel.objects.all()
    serializer_class = EarningSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)    # Non auth user can see records from this endpoint


class EarningCRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EarningModel.objects.all()
    serializer_class = EarningSerializer

