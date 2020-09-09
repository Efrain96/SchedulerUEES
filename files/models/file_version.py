""""""
from django.db import models

from main.models import PlanModel
from utils.models import TimeStampModel


class FilVersionModel(TimeStampModel):
    plan = models.ForeignKey(
        PlanModel, help_text="Planificacion",
        verbose_name="Planificacion",
        on_delete=models.CASCADE
    )
    academic_period = models.CharField(
        max_length=150, verbose_name="Periodo academico", help_text='Periodo académico',
        blank=True, null=True, default=''
    )
    generation_date = models.DateField(
        verbose_name="Fecha generación", null=True, blank=True,
        help_text='Fecha de generación'
    )
    version = models.CharField(max_length=150, verbose_name='Version', help_text='Version de archivo')

    class Meta:
        verbose_name = 'Archivo versión'
        verbose_name_plural = 'Archivos versión'
        db_table = 'archivos_version'
