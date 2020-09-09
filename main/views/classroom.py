from rest_framework.viewsets import ModelViewSet

from main.models import ClassRoomModel
from main.serializers import ClassRoomSerializer


class ClassroomViewSet(ModelViewSet):
    queryset = ClassRoomModel.objects.filter(status=True)
    serializer_class = ClassRoomSerializer
