import re
from django.db import models
from django.core.validators import validate_email
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

from validadores.validar_info import (
    validate_name,
    validate_cpf,
    validate_cgm,
    validate_phone,
)


class User(AbstractUser):
    LEITOR = 0
    FUNCIONARIO = 1
    BIBLIOTECARIO = 2

    STATUS_ATIVO = 0
    STATUS_BLOQUEADO = 1
    STATUS_SUSPENSO = 2

    USERS_TYPES_LIST = [
        (LEITOR, "Leitor"),
        (FUNCIONARIO, "Funcionário"),
        (BIBLIOTECARIO, "Bibliotecário"),
    ]

    STATUS_CHOICES = [
        (STATUS_ATIVO, "Ativo"),
        (STATUS_BLOQUEADO, "Bloqueado"),
        (STATUS_SUSPENSO, "Suspenso"),
    ]

    type_user = models.PositiveSmallIntegerField(
        choices=USERS_TYPES_LIST, default=LEITOR, verbose_name="Tipo de Usuário"
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES, default=STATUS_ATIVO, verbose_name="Status"
    )
    last_modified_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="modifier",
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Nome Completo",
        validators=[validate_name],
        help_text="Digite seu nome e sobrenome com letra maiúscula no começo",
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF",
        validators=[MinLengthValidator(11), validate_cpf],
        help_text="Não use pontos nem traços",
    )
    phone = models.CharField(
        max_length=11,
        verbose_name="Telefone",
        validators=[MinLengthValidator(10), validate_phone],
        help_text="Digite seu número de celular ou telefone fixo, adicione também seu DDD.",
    )
    cgm = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        unique=True,
        verbose_name="CGM",
        validators=[validate_cgm],
        help_text="Código Geral de Matrícula (10 dígitos)",
    )
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "phone", "cpf"]

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

        ordering = ["type_user", "username"]

    def __str__(self):
        return self.username

    def clean_email(self):
        email = self.email.lower().strip()
        if User.objects.filter(email=email).exclude(pk=self.pk).exists():
            raise ValidationError("O Email já está em uso")
        return email

    def phone_formatted(self):
        phone = self.phone
        if len(phone) == 11:
            return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"
        return f"({phone[:2]}) {phone[2:6]}-{phone[6:]}"

    def cpf_formatted(self):
        cpf = self.cpf
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" if cpf else ""
    
    def cpf_formatted_encrypted(self):
        cpf = self.cpf
        esconde = "*" * 3
        return f"{cpf[:3]}.{esconde}.{esconde}-{cpf[9:]}"


class UserChangeLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="change_logs")
    changed_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="changes_made"
    )
    change_date = models.DateTimeField(auto_now_add=True)
    field_changed = models.CharField(max_length=50)
    old_value = models.TextField()
    new_value = models.TextField()
    change_type = models.CharField(max_length=20)  # 'create', 'update', 'status_change'

    class Meta:
        ordering = ["-change_date"]
        verbose_name = "Registro de Alteração"
        verbose_name_plural = "Registros de Alteração"

    def __str__(self):
        return (
            f"{self.change_date} - {self.field_changed} alterado por {self.changed_by}"
        )
