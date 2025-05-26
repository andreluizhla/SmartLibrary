# "Palavra" + "Algo" => "PalavraAlgo" (concatenação) (dois textos)
# 2 + 2 = 4 (soma matemática) (dois números inteiros)
# "2" + "2" = "22"
# "" = texto

# Tipos Primitivos:
# str = string = texto
# int = inteiro
# float = números com um ponto flutuante = 3.1415
# bool = booleano = verdadeiro ou falso (True or False)

# () [] {}

# () => tuplas = listas que não mudam = listas constantes
# Exemplo:
# precos_tupla = (13.4, 10.5, 15.9)
# precos_tupla.append(20) -> erro: não é possível adicionar mais itens


# [] => listas = podem receber mais itens dentro deles
# Exemplo:
# precos_lista = ["13.4", "10.5", "15.9"]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, ...]
# [..., -8, -7, -6, -5, -4, -3, -2, -1]

# print(precos_lista[-2] + precos_lista[-1])

# print(precos_lista)
# precos_lista.append(20)
# print(precos_lista)

# {} => dicionário
# definição : valor
# maçã : é uma fruto que nasce em uma...

# precos_dicionario = {
#     "Lupa" : 10,
#     "Cubo Mágico" : 1.99,
#     "Amendoins" : 5,
# }

# print(precos_dicionario)

# print(precos_dicionario["Cubo Mágico"])


# Verificar se em uma boate essa pessoa pode entrar ou não
#  1= --> atribuição => idade recebe 17
# 2= --> igualdade => 2 == 3 => Verdadeiro ou Falso

# Testes Lógicos:
# == -> isso é igual a algo
# < = menor que
# > = maior que
# <= -> menor ou igual a
# >= -> maior ou igual a
# != -> negar algo -> diferente

# se = if
# senão = else
# senão + se = else + if = elif

# junção de condições:
# e -> and -> o resultado é verdadeiro se as duas condições forem veradeiras, caso contrário, é falso
# ou -> or -> o resultado é verdadeiro se pelo menos uma das condições forem veradadeiras, caso contrário é falso.
# não -> not -> inverte a lógica, se a entrada é verdadeiro a saída é falso e vice-versa

# if condição:
# resultado se verdadeiro
# elif condição:
# resultado se a última verificação for falsa e essa verificação for vedadeira
# else:
# Se todas as verificações forem falsas, esse comando será executado.

# Laços de repetição
# enquanto = while

# numero = int(input("Digite um número: "))

# while True:
#     numero = int(input("Digite outro número: "))
#     if numero == 999:
#         break


# for cont in range(1, 31):
#     numero = int(input(f"Digite um número na posição {cont}: "))

# variavel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, ..., 29]

# função
# fórmula para criar uma função:
# def nome_funcao

# ()
# ** = potência
# // = divisão inteira
# % = resto da divisão
# * = multiplicação
# / = divisão
# - = subtração
# + = adição

# print(type(2 + 3 / 3))

# numero = int(input("Digite um número: "))

# if numero % 2 == 0:
#     print("Esse número é par")
# else:
#     print("Esse número é ímpar")


# def comprar_pao(valor: float) -> float:
#     pao_preco = 1.5
#     num_pao = valor // pao_preco
#     troco = valor % pao_preco
#     return num_pao

# print(comprar_pao(1.6))


# class Cao:
#     def __init__(self, nome, comida, soneca):
#         self.nome = nome
#         self.comida = comida
#         self.soneca = soneca

#     def comer(self):
#         self.comida = self.comida - 1
#         print("O cão comeu!")
#         return self.comida

#     def dormir(self):
#         if self.soneca == True:
#             self.soneca = False
#             print("O cão dormiu!")
#         return self.soneca


# cao_1_nome = "José"
# cao_1_comida = 5
# cao_1_soneca = True

# cao_2_nome = "Maria"
# cao_2_comida = 2
# cao_2_soneca = False

# def comer(comida):
#     comida = comida - 1
#     return comida

# comer(cao_1_comida)

# cao_1 = Cao("José", 5, True)
# cao_2 = Cao("Maria", 2, False)
# cao_3 = Cao("Felipe", 10, False)
# cao_4 = Cao("Mauro", 3, True)
# cao_5 = Cao("Maísa", 5, True)
# cao_1.dormir()
# cao_2.comer()
# cao_3.comer()
# cao_4.dormir()


# Terciera Aula:


# algo = "Algo"

# print(f"Algo é: {algo}")

variavel = "93274890"

# Tipos primitos:
# texto = "" / '' -> string -> str
# numeros inteiros = 93420432 -> int
# números decimais = 3.141592 -> float
# boleano = Verdadeiro / Falso -> bool
# Vazio = Null


# variavel = input("Coloque seu nome: ")
# if variavel == "Mauro" or variavel == "André":
#     print("Olá Dev!")
# else:
#     print("Olá!")


# junções de condições:
# numero == 0 -> 0
# numero > 0 -> 1, 2, 3, 4, 5, ... Verdadeiro
# numero < 0 -> ..., -5, -4, -3, -2, -1 Verdadeiro
# numero >= 0 -> 0, 1, 2, ...
# numero <= 0 -> ..., -2, -1, 0

# idade = 60

# if idade > 17 and idade < 60:
#     print("Pode entrar!")
# else:
#     print("Não entre!")

# e -> and -> os dois tem que ser vedadeiros
# ou -> or -> qualquer um pode ser verdadeiro


# loops
# cont = 0
# while cont < 5:
#     print(cont)
#     cont += 1
#     # c = c + 1
#     # c++

# for item in lista:
#     print(item)

# lista = ("letras", 9, True, None)

dicionario = {
    "item1": "valor1",
    "item2": "valor2",
    "item3": "valor3",
    "item4": "valor4",
}

for item in dicionario:
    print(item)

# print(lista[-1])
# lista -> [0, 1, 2, 3, 4, ...]
# lista -> [..., -4, -3, -2, -1]

# print(dicionario["item1"])


