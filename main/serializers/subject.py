from rest_framework.serializers import ModelSerializer

from main.models import SubjectModel


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = ("name", "code")
