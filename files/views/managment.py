""""""
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView

from main.models import PlanModel
from utils.general_functions import generate_file_


class IbmPlanListView(ListView):
    model = PlanModel
    queryset = PlanModel.objects.filter(status=True)
    template_name = "files/list-ibm.html"
    context_object_name = 'planns'


def generate_document(request):
    if request.method == "POST":
        id = request.POST.get("id")
        target_format = request.POST.get("format")  # Obtener desde frontend
        instance = get_object_or_404(PlanModel, pk=id)
        # if instance.state is False:
        #     messages.error(request, "No puede generar documento para IBM.")
        #     return HttpResponseRedirect(reverse_lazy('main:list-scheduler'))

        # 1.- Parsear la data que corresponde
        content = generate_file_(instance=instance, data=instance.lineitemschedulemodel_set.all(), format=target_format)
        messages.success(request, "El fichero seleccionado ha sido generado exitosamente.")
        response = HttpResponse(content, content_type='application/txt')
        response['Content-Disposition'] = 'attachment; filename="' + target_format + '.txt"'
        return response
    return HttpResponseRedirect(reverse_lazy('files:list-ibm'))
