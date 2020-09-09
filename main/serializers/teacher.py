""""""

from rest_framework.serializers import ModelSerializer

from main.models import TeacherModel


class TeacherModelSerializer(ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = (
            "full_name", "alias", "contract",
            "affinity", "skill"
        )
