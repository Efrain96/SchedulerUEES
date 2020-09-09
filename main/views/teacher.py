# Import django libraries
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

# Import utilities
from rest_framework.viewsets import ModelViewSet
from main.serializers.teacher import TeacherModelSerializer
from main.models import TeacherModel


class TeacherListView(ListView):
    model = TeacherModel
    template_name = 'main/list-teacher.html'
    ordering = ['-created']
    context_object_name = 'teachers'
    queryset = TeacherModel.objects.filter(status=True)


class TeacherDeleteView(DeleteView):
    model = TeacherModel
    success_url = reverse_lazy("main:list-teachers")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        return HttpResponseRedirect(self.get_success_url())


class TeacherViewSet(ModelViewSet):
    queryset = TeacherModel.objects.filter(status=True)
    serializer_class = TeacherModelSerializer
