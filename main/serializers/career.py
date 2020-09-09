""""""

from rest_framework.serializers import ModelSerializer

from main.models import CareerModel


class CareerSerializer(ModelSerializer):
    class Meta:
        model = CareerModel
        fields = ("name", "code", "alias")
