from django.db import models
from django.core.exceptions import ValidationError

from .validators import id_code_validator


class CollectionItem(models.Model):
    ESTADO_CONSEVACAO = {
        "Bom": "Bom",
        "Regular": "Regular",
        "Ruim": "Ruim",
        "Danificado": "Danificado",
    }
    ESTADO_DISPONIVEL = {
        "Disponível": "Disponível",
        "Emprestado": "Emprestado",
        "Reservado": "Reservado",
        "Danificado": "Danificado",
    }
    title = models.CharField(
        verbose_name="Título da Obra",
        max_length=50,
        null=False,
        blank=False,
    )
    id_code = models.CharField(
        verbose_name="Código Identificador",
        max_length=10,
        primary_key=True,
        validators=[id_code_validator],
    )
    preservation = models.CharField(
        verbose_name="Estado de Consevação",
        max_length=10,
        choices=ESTADO_CONSEVACAO,
        null=False,
        blank=False,
    )
    availability = models.CharField(
        verbose_name="Disponibilidade",
        max_length=10,
        choices=ESTADO_DISPONIVEL,
        null=False,
        blank=False,
    )
    entry_date = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False,
    )
    
    class Meta:
        ordering = ['title']
