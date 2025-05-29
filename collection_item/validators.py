import re
from django.core.exceptions import ValidationError


def id_code_validator(value):
    id_code = value

    if len(id_code) != 10:
        raise ValidationError("O código tem que conter 10 números")

    if not re.fullmatch(r"\d+", id_code):
        raise ValidationError(
            "O Código de Identificação não pode conter espaços, letras ou símbolos"
        )


def validate_name(value):
    name = value

    if re.search(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]", name):
        raise ValidationError("O nome não pode conter números ou símbolos")
