from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .validators import id_code_validator, validate_name

User = get_user_model()


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
        verbose_name="Estado de Conservação",
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
        ordering = ["title"]
        verbose_name = "Item do Acervo"
        verbose_name_plural = "Itens do Acervo"

    def __str__(self):
        return f"{self.title} ({self.id_code})"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            try:
                original = CollectionItem.objects.get(pk=self.pk)
                if original.availability != self.availability:
                    ItemStatusChange.objects.create(
                        item=self,
                        previous_status=original.availability,
                        new_status=self.availability,
                        changed_by=getattr(self, "responsavel_form_input", "Sistema"),
                    )
            except CollectionItem.DoesNotExist:
                pass
        super().save(*args, **kwargs)


class ItemStatusChange(models.Model):
    item = models.ForeignKey(
        CollectionItem, on_delete=models.CASCADE, related_name="status_changes"
    )
    previous_status = models.CharField(max_length=10, verbose_name="Status Anterior")
    new_status = models.CharField(max_length=10, verbose_name="Novo Status")
    changed_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Data da Alteração"
    )
    changed_by = models.CharField(
        max_length=100,
        verbose_name="Responsável pela Alteração",
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ["-changed_at"]
        verbose_name = "Alteração de Status"
        verbose_name_plural = "Alterações de Status"

    def __str__(self):
        return f"{self.item} alterado por {self.changed_by} em {self.changed_at}"
