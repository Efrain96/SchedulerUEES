""""""

# import utilities
from django.db import models

from utils.models import TimeStampModel


class CareerModel(TimeStampModel):
    name = models.CharField(max_length=200, verbose_name="Nombre", help_text="Nombre de la carrera")
    code = models.CharField(max_length=100, verbose_name="Código", help_text="Código de carrera")
    alias = models.CharField(
        max_length=50, verbose_name="Alias",
        help_text="Campo referencial ej: C-2020.",
        default="", blank="", null=""
    )

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        db_table = "carrera"

    def __str__(self):
        return "[{}] {}".format(self.code, self.name)
