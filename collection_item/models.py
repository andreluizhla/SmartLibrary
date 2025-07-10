from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from .validators import id_code_validator

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
        verbose_name = "Item do Acervo"
        verbose_name_plural = "Itens do Acervo"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.id_code})"

    def save(self, *args, **kwargs):
        if self.pk is not None:
            try:
                original = CollectionItem.objects.get(pk=self.pk)
                if original.availability != self.availability:
                    changed_by = getattr(self, "responsavel_form_input", "Sistema")
                    ItemStatusChange.objects.create(
                        item=self,
                        previous_status=original.availability,
                        new_status=self.availability,
                        changed_by=changed_by,
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
    changed_at = models.DateTimeField(verbose_name="Data da Alteração", default=now)
    changed_by = models.CharField(
        max_length=150,
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


class DelayPolicy(models.Model):
    max_days = models.PositiveIntegerField(
        verbose_name="Prazo maximo de emprestimo", null=False, blank=False
    )
    fine_value = models.FloatField(
        verbose_name="Valor da multa por dias de atraso", null=False, blank=False
    )
    delay_tolerance = models.PositiveIntegerField(
        verbose_name="Tolerância de atraso", null=True, blank=True
    )
    item_limits = models.PositiveIntegerField(
        verbose_name="Limite de itens simultâneos", null=False, blank=False
    )
