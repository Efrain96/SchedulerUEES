""""""

# import utilities
from django.db import models

from utils.models import TimeStampModel


class ClassRoomModel(TimeStampModel):
    name = models.CharField(max_length=200, verbose_name="Nombres", help_text="Nombres completos")
    code = models.CharField(
        max_length=10, verbose_name="Codigo",
        help_text="Código referencial del contrato. Ej: A01-2"
    )
    capacity = models.PositiveSmallIntegerField(verbose_name="Capacidad")
    affinity = models.PositiveSmallIntegerField(
        verbose_name="Afinidad", default=1, blank=True
    )

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aulas"
        db_table = "aula"

    def __str__(self):
        return "{}".format(self.code)
