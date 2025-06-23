import re
from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from .validar_info import (
    validate_name,
    validate_cpf,
    validate_cgm,
    validate_phone,
    validate_password,
)


class User(AbstractUser):
    LEITOR = 0
    FUNCIONARIO = 1
    BIBLIOTECARIO = 2

    USER_TYPES = [
        (LEITOR, "Leitor"),
        (FUNCIONARIO, "Funcionário"),
        (BIBLIOTECARIO, "Bibliotecário"),
    ]

    type_user = models.PositiveSmallIntegerField(
        choices=USER_TYPES, default=LEITOR, verbose_name="Tipo de Usuário"
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
        help_text="Digite apenas números, sem pontuações ou espaços.",
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

    def __str__(self):
        return self.username

    def get_tipo_usuario_display(self):
        """Retorna o label correspondente ao número armazenado"""
        for numero, label in self.USERS_TYPES_LIST:
            if numero == self.type_user:
                return label
        return 0

    def clean_email(self):
        email = self.email.lower().strip()
        if User.objects.filter(email=email).exclude(pk=self.pk).exists():
            raise ValidationError("O Email já está em uso")
        return email

    def cpf_formatted(self):
        cpf_limpo = re.sub(r"[^0-9]", "", self.cpf)
        return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
