""""""

# import utilities
from django.db import models

from utils.models import TimeStampModel


class BasicParallelModel(TimeStampModel):
    code = models.CharField(max_length=50, verbose_name="Alias", help_text="B.")
    description = models.TextField(default='', verbose_name="Descripción", help_text="Referencia sobre el paralelo.")

    class Meta:
        verbose_name = "Base paralelo"
        verbose_name_plural = "Base paralelos"
        db_table = "base_paralelo"


class ParallelModel(TimeStampModel):
    name = models.PositiveSmallIntegerField(default=1, verbose_name="Nombre", help_text="Ej: 1, 2, 3, etc.")
    code = models.CharField(
        max_length=20, verbose_name="Codigo",
        help_text="Codigo referencial del paralelo. Opcional",
        null=True, blank=True
    )
    term = models.ForeignKey(
        'TermModel', verbose_name="Periodo",
        on_delete=models.CASCADE,
        related_name='term_parallels'
    )
    plan = models.ForeignKey(
        'PlanModel', verbose_name="Planificación",
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='plan_parallels'
    )
    teacher = models.ForeignKey(
        'TeacherModel', verbose_name="Profesor",
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='assigned_parallels'
    )
    subject_mesh = models.ForeignKey(
        'SubjectMeshModel',
        verbose_name="Materia Malla",
        on_delete=models.SET_NULL, null=True, blank=True,
        related_name='parallels_subject_mesh'
    )
    classroom = models.ForeignKey(
        'ClassRoomModel', verbose_name="Aula",
        related_name="class_parallels",
        on_delete=models.SET_NULL, help_text="Selecciona aula.",
        null=True, blank=True
    )

    class Meta:
        verbose_name = "Paralelo"
        verbose_name_plural = "Paralelos"
        db_table = "paralelo"

    def __str__(self):
        return "{}".format(self.name)
