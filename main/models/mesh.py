""""""

# Import django libraries
from django.db import models

# import utilities
from main.models import SubjectMeshModel, CareerModel
from utils.models import TimeStampModel


class MeshModel(TimeStampModel):
    name = models.CharField(max_length=200, verbose_name="Nombres", help_text="Nombres completos")
    career = models.ForeignKey(
        CareerModel, verbose_name="Carrera", on_delete=models.CASCADE,
        related_name='careers'
    )
    subject_mesh = models.ForeignKey(
        SubjectMeshModel, verbose_name="Materia Malla", help_text="Nivel",
        on_delete=models.SET_NULL, null=True, blank=True, related_name='levels'
    )
    year = models.PositiveSmallIntegerField(verbose_name="Año")

    class Meta:
        verbose_name = "Malla"
        verbose_name_plural = "Mallas"
        db_table = "malla"

    def __str__(self):
        return f"Carrera: [{self.career.code}], {self.name}"
