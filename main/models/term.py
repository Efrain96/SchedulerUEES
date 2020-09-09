""""""

# import utilities
from django.db import models

from utils.models import TimeStampModel


class TermModel(TimeStampModel):
    name = models.CharField(max_length=120, verbose_name="Nombre", help_text="Nombres completos")
    year = models.PositiveSmallIntegerField(verbose_name="Año", default=2020, help_text="")

    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"
        db_table = "periodo"

    def __str__(self):
        return "{} - {}".format(self.name, self.year)
