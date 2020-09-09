"""Module that models."""

# Import django libraries
from enum import Enum

from django.db import models

# Import utilities
from utils.models import TimeStampModel


def label_format(instance):
    """

    :param instance:
    :return:
    """
    if instance.num_end_day:
        label_schedule = f"[{instance.display_day(instance.num_start_day)} y " \
                         f"{instance.display_day(instance.num_end_day)}] de " \
                         f"{instance.start_time.strftime('%HH:%M')} a {instance.end_time.strftime('%HH:%M')}"
    else:
        label_schedule = f"[{instance.display_day(instance.num_start_day)}] " \
                         f"{instance.start_time.strftime('%HH:%M')} a {instance.end_time.strftime('%HH:%M')}"
    return label_schedule


class TimeAvailabilityModel(TimeStampModel):
    WEEK_CHOICES = (
        ("1", "Lunes"),
        ("2", "Martes"),
        ("3", "Miércoles"),
        ("4", "Jueves"),
        ("5", "Viernes"),
        ("6", "Sábado"),
    )
    term = models.ForeignKey(
        'TermModel',
        on_delete=models.CASCADE,
        verbose_name="Periodo", help_text="Periodo",
        related_name='assigned_term'
    )
    teachers = models.ForeignKey(
        "TeacherModel", verbose_name="Profesor",
        help_text="Seleccione profesor",
        on_delete=models.CASCADE,
        related_name='availabilities'
    )
    day = models.DateField(
        verbose_name="Día", null=True, blank=True,
        help_text="Fecha disponibilidad"
    )
    num_start_day = models.CharField(
        max_length=5, verbose_name="Día 1", help_text="Día inicial. Ej: Lunes.",
        choices=WEEK_CHOICES, default="1"
    )
    num_end_day = models.CharField(
        max_length=5, verbose_name="Día 2", help_text="Segundo día. Ej: Jueves.",
        choices=WEEK_CHOICES, null=True, blank=True
    )
    start_time = models.TimeField(
        verbose_name="Hora inicio"
    )
    end_time = models.TimeField(
        verbose_name="Hora fin"
    )
    description = models.CharField(max_length=200, verbose_name="Descripcion", null=True, blank=True)

    class Meta:
        verbose_name = 'Disponibilidad horaria'
        verbose_name_plural = 'Disponibilidad horaria'
        db_table = 'disponibilidad_horaria'

    def __str__(self):
        return label_format(self)

    def display_day(self, num_day):
        if num_day:
            for item in self.WEEK_CHOICES:
                if item[0] == num_day:
                    return item[1]
        return ""

    def save(self, *args, **kwargs):
        self.description = label_format(self)
        super().save(*args, **kwargs)
