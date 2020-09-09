""""""

# import utilities
from django.db import models

from utils.models import TimeStampModel


class ContractModel(TimeStampModel):
    name = models.CharField(max_length=200, verbose_name="Nombres", help_text="Nombres completos")
    code = models.CharField(
        max_length=10, verbose_name="Codigo",
        help_text="Código referencial del contrato. Ej: COD001")

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
        db_table = "contrato"

    def __str__(self):
        return "[{}] {}".format(self.code, self.name)
