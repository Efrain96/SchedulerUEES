from rest_framework.viewsets import ModelViewSet

from main.models import CareerModel
from main.serializers import CareerSerializer


class CareerViewSet(ModelViewSet):
    queryset = CareerModel.objects.filter(status=True)
    serializer_class = CareerSerializer
