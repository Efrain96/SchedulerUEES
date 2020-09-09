""""""
from datetime import datetime

# Import django libraries
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction, IntegrityError
from django.forms import formset_factory, inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView

# Import utilities
from main.forms import BasicSchedulerForm, SchedulerLineItemFormSet, LineForm
from main.models import PlanModel, LineItemScheduleModel


class SchedulerListView(LoginRequiredMixin, ListView):
    model = PlanModel
    template_name = 'main/list-scheduler.html'
    ordering = ['-created']
    context_object_name = 'planns'
    queryset = PlanModel.objects.filter(status=True)


@login_required(login_url="/login/")
def create_scheduler(request):
    data_line = []
    form = BasicSchedulerForm()
    # Create the formset, specifying the form and formset we want to use.
    LineItemFormSet = formset_factory(LineForm, formset=SchedulerLineItemFormSet, extra=2)
    if request.method == 'POST':
        form = BasicSchedulerForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                instance = form.save()
                formset = LineItemFormSet(request.POST, prefix='scheduler-detail')
                if formset.is_valid():
                    lineitems = formset.cleaned_data
                    for line in lineitems:
                        line['plan'] = instance
                        data_line.append(
                            LineItemScheduleModel(**line)
                        )
                    try:
                        LineItemScheduleModel.objects.bulk_create(data_line)
                        messages.success(request, "Planificación guardada exitosamente!")
                    except IntegrityError:
                        messages.error(request, "Error al guardar la planificación.")
                    return HttpResponseRedirect(reverse_lazy('main:list-scheduler'))

                else:
                    feedback_message = "Error al guardar la planificación."
                    messages.error(request, feedback_message)
        else:
            error_data = form.errors.as_data()
            error_elements = []
            for err in list(error_data.keys()):
                s = f"{err}: {error_data[err][0].__str__()}."
                error_elements.append(s)
            feedback_message = "Error al en los siguientes campos| " + " ".join(error_elements)
            messages.error(
                request,
                feedback_message
            )
    else:
        formset = LineItemFormSet(initial={}, prefix='scheduler-detail')
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'main/create-scheduler.html', context)


@login_required(login_url="/login/")
def edit_scheduler(request, id):
    instance = get_object_or_404(PlanModel, pk=id)

    if instance.state:
        messages.error(request, "No puede editar la planificación debido a que ya ha sido validada.")
        HttpResponseRedirect(reverse_lazy('main:list-scheduler'))

    form = BasicSchedulerForm(
        initial={
            "term": instance.term,
            "career": instance.career,
        }
    )
    LineItemFormSet = inlineformset_factory(
        PlanModel,
        LineItemScheduleModel, extra=0,
        fields=("id", "subject", "teacher", "classroom", "parallel", "start_day", "start_time", "end_time"),
        widgets={
            'start_time': forms.TimeInput(format='%I:%M %p', attrs={"class": "time form-control timepicker"}),
            'end_time': forms.TimeInput(format='%I:%M %p', attrs={"class": "time form-control timepicker"}),
        }
    )

    formset = LineItemFormSet(instance=instance, prefix='scheduler-detail')
    if request.method == "POST":
        form = BasicSchedulerForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                data_basic = form.cleaned_data
                instance = PlanModel(id=id, **data_basic, created=datetime.now())
                formset = LineItemFormSet(request.POST, instance=instance, prefix='scheduler-detail')
                if formset.is_valid():
                    instance.save()
                    formset.save()
                    messages.success(request, "La planificación ha sido modificada exitosamente.")
                    return HttpResponseRedirect(reverse_lazy('main:list-scheduler'))
                else:
                    messages.error(request, "Error al ingresar los datos de la planificación.")
        else:
            messages.error(request, "Existen error al ingresar la información básica de la planificación")
    context = {
        'form': form,
        'formset': formset
    }
    return render(request, 'main/edit-scheduler.html', context)


@login_required(login_url="/login/")
def change_state(request):
    if request.method == "POST":
        id = request.POST['id']
        instance = get_object_or_404(PlanModel, pk=id)
        if instance:
            instance.state = True
            instance.modified = datetime.now()
            instance.save()
            messages.success(request, "Planificación verficada")
            return HttpResponseRedirect(reverse_lazy('main:list-scheduler'))
        return HttpResponseRedirect(reverse_lazy('main:list-scheduler'))
    return HttpResponseRedirect(reverse_lazy('main:list-scheduler'))


class DetailSchedulerView(LoginRequiredMixin, DetailView):
    model = PlanModel
    template_name = 'main/detail-scheduler.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.get_object()
        context["items"] = LineItemScheduleModel.objects.filter(status=True, plan=instance)
        return context


class DeleteSchedulerView(LoginRequiredMixin, DeleteView):
    model = PlanModel
    context_object_name = "obj"
    template_name = "main/object_confirm_delete.html"
    success_url = reverse_lazy("main:list-scheduler")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.soft_delete()
        messages.success(request, "La planificación ha sido eliminada exitosamente.")
        return HttpResponseRedirect(self.get_success_url())
