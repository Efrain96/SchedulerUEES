""""""
from django.db import models

from utils.models import TimeStampModel


class IbmScheduleModel(TimeStampModel):
    file_version = models.ForeignKey(
        'FilVersionModel', verbose_name='Archivo version', on_delete=models.CASCADE
    )
    day_week = models.PositiveSmallIntegerField(verbose_name='Día semana')
    start_time = models.TimeField(verbose_name='Hora inicio')
    end_time = models.TimeField(verbose_name='Hora Fin')
    assigned_teacher = models.CharField(max_length=150, verbose_name='Profesor asignado')
    assigned_classroom = models.CharField(max_length=150, verbose_name='Aula asignada')

    class Meta:
        verbose_name = 'IBM Horario'
        verbose_name_plural = 'IBM Horarios'
        db_table = 'horario_ibm'
