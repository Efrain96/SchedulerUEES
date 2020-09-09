""""""
from django.db import models

# Import utilities
from utils.models import TimeStampModel


class FilVersionDetailModel(TimeStampModel):
    file_version = models.ForeignKey(
        'FilVersionModel',
        verbose_name='Archivo version',
        help_text="Archivos de version.",
        on_delete=models.CASCADE
    )
    name_file = models.CharField(max_length=100, verbose_name='Nombre Archivo')
    type_file = models.CharField(max_length=150, verbose_name="Tipo archivo", default='')
    generate_file = models.FileField(verbose_name='Archivo generado', null=True, blank=True)

    class Meta:
        verbose_name = 'Archivo version detalle'
        verbose_name_plural = 'Archivos version detalles'
        db_table = 'archivos_version_detalle'
