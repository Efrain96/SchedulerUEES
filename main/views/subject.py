""""""

# Import django libraries
from django.views.generic import ListView

# Import utilities
from rest_framework.viewsets import ModelViewSet

from main.models import SubjectModel
from main.serializers import SubjectSerializer


class SubjectListView(ListView):
    model = SubjectModel
    template_name = 'main/list-subject.html'
    ordering = ['-created']
    context_object_name = 'subjects'
    queryset = SubjectModel.objects.filter(status=True)


class SubjectViewSet(ModelViewSet):
    queryset = SubjectModel.objects.filter(status=True)
    serializer_class = SubjectSerializer
