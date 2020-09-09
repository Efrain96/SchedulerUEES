""""""

# import django libraries
from django.db import models
from django.utils import timezone

# import utilities
from main.models import CareerModel, ContractModel
from utils.models import TimeStampModel


class TeacherModel(TimeStampModel):
    full_name = models.CharField(max_length=200, verbose_name="Nombres", help_text="Nombres completos")
    alias = models.CharField(max_length=20, verbose_name="Alias", help_text="Nombre referencial al profesor. Ej: CH")
    contract = models.ForeignKey(
        ContractModel, verbose_name="Contrato", on_delete=models.SET_NULL, null=True,
        related_name="contracts"
    )
    career = models.ForeignKey(
        CareerModel, verbose_name="Carrera", on_delete=models.CASCADE,
        related_name="assigned_career"
    )
    affinity = models.PositiveSmallIntegerField(
        default=1, verbose_name="Afinidad", blank=True, help_text="Afinidad del profesor [1-10]"
    )
    skill = models.PositiveSmallIntegerField(
        default=1, verbose_name="Habilidad", blank=True,
        help_text="Calificacion, destreza profesor [1-10]"
    )

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        db_table = "profesor"

    def soft_delete(self):
        self.status = False
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return "[{}] {}".format(self.alias, self.full_name)
