""""""

# import django libraries
from django.db import models

# import utilities
from utils.models import TimeStampModel


class SubjectMeshModel(TimeStampModel):
    subject = models.ForeignKey(
        'SubjectModel',
        verbose_name='Materia',
        on_delete=models.SET_NULL,
        null=True,
        help_text="Materia."
    )
    level = models.IntegerField(default=1, verbose_name="Nivel", help_text="Nivel carrera.")

    class Meta:
        verbose_name = "Materia Malla"
        verbose_name_plural = "Materias Malla"
        db_table = "materia_malla"

    def __str__(self):
        return "Nivel {}-{}".format(self.level, self.subject.name)
