""""""

from rest_framework.serializers import ModelSerializer

from main.models import ClassRoomModel


class ClassRoomSerializer(ModelSerializer):
    class Meta:
        model = ClassRoomModel
        fields = ("name", "code", "capacity", "affinity")
