import re
from django.core.exceptions import ValidationError


def validate_cpf(value):
    cpf = re.sub(r"[^0-9]", "", value)

    if len(cpf) != 11:
        raise ValidationError("CPF deve conter 11 dígitos")

    if cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido (dígitos repetidos)")

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = 11 - (soma % 11)
    digito1 = resto if resto < 10 else 0

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = 11 - (soma % 11)
    digito2 = resto if resto < 10 else 0

    if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
        raise ValidationError("CPF inválido (dígitos verificadores incorretos)")


def validate_cgm(value):
    cgm = re.sub(r"[^0-9]", "", value)

    if len(cgm) != 10:
        raise ValidationError("CGM deve conter 10 dígitos")

    if not cgm.isdigit():
        raise ValidationError("CGM deve contér apenas números")


def validate_phone(value):
    phone = re.sub(r"[^0-9]", "", value)

    if len(phone) not in (10, 11):
        raise ValidationError("Número deve conter 10 (fixo) ou 11 (celular) dígitos")

    ddd = phone[:2]
    number = phone[2:]

    if int(ddd) not in ddd_list:
        raise ValidationError("DDD inválido")

    if len(phone) == 11 and not number.startswith("9"):
        raise ValidationError("Celulares devem começar com 9 (ex: 9XXXX-XXXX)")

    print(not phone.isdigit())
    print(phone)
    if not phone.isdigit():
        raise ValidationError("Número deve conter apenas números")


ddd_list = [
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    21,
    22,
    24,
    27,
    28,
    31,
    32,
    33,
    34,
    35,
    37,
    38,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    51,
    53,
    54,
    55,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    71,
    73,
    74,
    75,
    77,
    79,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
]

# DDD dos 26 estados + Distrito Federal do Brasil:
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# PQP, quanto DDD
