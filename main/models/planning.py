""""""

# import utilities
from datetime import datetime

from django.db import models

from utils.models import TimeStampModel


class PlanModel(TimeStampModel):
    version = models.CharField(max_length=20, verbose_name='Version', default='', blank=True,
                               help_text='Version de la planificacion')
    date_emi = models.DateField(verbose_name='Fecha', null=True)
    term = models.ForeignKey('TermModel', verbose_name="Periodo", on_delete=models.CASCADE)
    career = models.ForeignKey('CareerModel', verbose_name="Carrera", on_delete=models.CASCADE)
    state = models.BooleanField(default=False, verbose_name='Estado', help_text='Estado de planificación.')

    class Meta:
        verbose_name = "Planificación"
        verbose_name_plural = "Planificaciones"
        db_table = "planificacion"

    def __setstate__(self, state):
        if state is False:
            self.lineitemschedulemodel_set.filter(plan=self).update(status=False)
        else:
            self.lineitemschedulemodel_set.filter(plan=self).update(status=True)

    def soft_delete(self):
        self.status = False
        self.deleted_at = datetime.now()
        self.save()

    def get_cancel_url(self):
        return '/planificaciones/'

    def __str__(self):
        return "{} {}-{}".format(self.version, self.term, self.career)


class LineItemScheduleModel(TimeStampModel):
    plan = models.ForeignKey(
        PlanModel,
        verbose_name='Planificacion',
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        'SubjectModel',
        verbose_name="Materia",
        on_delete=models.CASCADE
    )
    teacher = models.ForeignKey(
        'TeacherModel',
        verbose_name='Profesor',
        help_text='Seleccione profesor(a)',
        on_delete=models.CASCADE
    )
    classroom = models.ForeignKey(
        'ClassRoomModel',
        verbose_name='Clase',
        help_text='Seleccionar el aula',
        on_delete=models.CASCADE
    )
    start_day = models.CharField(
        max_length=120, verbose_name="Día 1", help_text="Día para la planificacion",
        default='', null=True, blank=True)
    end_day = models.CharField(
        max_length=120, verbose_name="Día 2", help_text="Día para la planificacion",
        default='', null=True, blank=True)
    start_time = models.CharField(max_length=70,
                                  verbose_name="Hora inicio", null=True, blank=True, help_text="Hora inicio"
                                  )
    end_time = models.CharField(max_length=70,
                                verbose_name="Hora fin", null=True, blank=True, help_text="Hora fin"
                                )
    parallel = models.ForeignKey(
        'ParallelModel', verbose_name="Paralelo", on_delete=models.SET_NULL,
        null=True, blank=True, help_text='Seleccione paralelo', limit_choices_to={"status": True}
    )
    availability = models.ForeignKey(
        'TimeAvailabilityModel',
        verbose_name="Disponibilidad", on_delete=models.SET_NULL, blank=True,
        null=True,
        help_text='Disponibilidad horaria', limit_choices_to={"status": True}
    )

    class Meta:
        verbose_name = 'Item planificacion'
        verbose_name_plural = 'Items de planificacion'
        db_table = 'planificacion_item'
