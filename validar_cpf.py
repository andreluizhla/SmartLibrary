cpf = str(input("Digite o CPF (use somente números): "))

def validar_cpf(cpf: str) -> bool:
    digitos_verificadores = ''

    for n in range(-1, 1):
        soma = 0

        for c in range(1, 10):
            soma += int(cpf[c + n]) * c

        resultado = soma % 11

        digitos_verificadores += str(resultado)[-1]

    if len(cpf) == 11:
        if digitos_verificadores == (cpf[-2] + cpf[-1]):
            print(f"O CPF {cpf} é Válido!")
            return True
        else:
            print(f"O CPF {cpf} Não é válido!")
            return False
    else:
        print("O CPF informado está fora dos padrões")
        return False
# print(validarCPF(cpf))
# print(cpf[-2] + cpf[-1])