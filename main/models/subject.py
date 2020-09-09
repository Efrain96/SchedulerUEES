""""""

# import utilities
from django.db import models

from utils.models import TimeStampModel


class SubjectModel(TimeStampModel):
    name = models.CharField(max_length=200, verbose_name="Nombres", help_text="Nombres completos")
    code = models.CharField(max_length=50, verbose_name="Código", help_text="Código de la materia. Ej: MAT001")

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"
        db_table = "materia"

    def __str__(self):
        return "[{}] {}".format(self.code, self.name)
