import re
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .validar_info import (
    validate_name,
    validate_cpf,
    validate_cgm,
    validate_phone,
    validate_password,
)


class User(models.Model):
    name = models.CharField(
        verbose_name="Nome Completo",
        max_length=100,
        null=False,
        blank=False,
        validators=[validate_name],
        unique=True,
        help_text="Esse nome ficará no banco de dados da Secretaria de Educação do Paraná",
    )
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
        null=False,
        blank=False,
        primary_key=True,
        validators=[validate_cpf],
        help_text="Não use pontos nem traços",
    )
    cgm = models.CharField(
        verbose_name="CGM",
        max_length=10,
        null=False,
        blank=False,
        unique=True,
        validators=[validate_cgm],
        help_text="Código Geral de Matrícula (10 dígitos)",
    )
    email = models.EmailField(
        verbose_name="E-mail",
        max_length=50,
        null=False,
        blank=False,
        unique=True,
        validators=[validate_email],
        help_text="Use o @gmail ou o @escola",
    )
    phone = models.CharField(
        verbose_name="Telefone",
        max_length=11,
        validators=[validate_phone],
        help_text="Digite apenas números, sem pontuações ou espaços. Exemplo: Para (21) 99999-8888, digite 21999998888",
    )
    password = models.CharField(
        verbose_name="Senha",
        max_length=128,
        null=False,
        blank=False,
        validators=[validate_password],
        help_text="Coloque uma senha com no mínimo 8 caracteres",
    )

    def clean_email(self):
        super().clean()

    def cpf_formatted(self):
        cpf_limpo = re.sub(r"[^0-9]", "", self.cpf)
        return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
