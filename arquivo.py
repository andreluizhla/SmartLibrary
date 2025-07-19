# variavel = int()
# print(variavel)


# def soma(x, y):
#     resultado = x + y
#     return resultado

# # int()
# # float() -> "2" -> 2.0
# num1 = int(input("Escreva o primeiro numero: "))
# # texto
# # "" -> string
# # "1" + "2" -> "12"
# num2 = int(input("Escreva o segundo numero: "))
# print(soma(num1, num2))

# def win()

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

# variavel = "93274890"

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

# dicionario = {
#     "item1": "valor1",
#     "item2": "valor2",
#     "item3": "valor3",
#     "item4": "valor4",
# }

# for item in dicionario:
#     print(item)

# print(lista[-1])
# lista -> [0, 1, 2, 3, 4, ...]
# lista -> [..., -4, -3, -2, -1]

# print(dicionario["item1"])


# Comandos para o projeto SmartLibrary

# Comandos:
# pip install django
# pip install python-decouple
# pip install dj-database-url
# pip install black
# pip install crispy-bootstrap5

# Extensão Recomendada:
# SQLite Viewer
# Black Formatter
# MySQL por: Database Client

# {
#     "editor.formatOnSave": true,
#     "python.formatting.provider": "black",
#     "editor.defaultFormatter": "ms-python.black-formatter",
#     "files.associations": {
#         "**/templates/**/*.html": "django-html"
#     },
#     "emmet.includeLanguages": {
#         "django-html": "html"
#     }
# }

# Criar Ambiente Virtual
# python -m venv .venv

# Em seguida, TENTE o comando:
# .venv\Scripts\activate

# se ocorrer erro de permissão, execute o comando:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Execute novamente o penúltimo comando


# Criação de APPs:
# django-admin startapp [Nome do APP]
# ou
# python -m django startapp [Nome do APP]









# Código possívelmente útil:
# collection_item/models.py

# CollectionItem:
# [...]
# def save(self, *args, **kwargs):
#     if self.pk is not None:
#         try:
#             original = CollectionItem.objects.get(pk=self.pk)
#             if original.availability != self.availability:
#                 changed_by = getattr(self, "responsavel_form_input", "Sistema")
#                 # ItemStatusChange.objects.create(
#                 #     item=self,
#                 #     action=ItemStatusChange.ACTION_UPDATE,
#                 #     field_changed="availability",
#                 #     previous_value=str(original.availability),
#                 #     new_value=str(self.availability),
#                 #     changed_by=changed_by,
#                 # )
#         except CollectionItem.DoesNotExist:
#             pass
#     super().save(*args, **kwargs)



# class ItemStatusChange(models.Model):
#     ACTION_UPDATE = "update"
#     ACTION_DELETE = "delete"
#     ACTION_CHOICES = [
#         (ACTION_UPDATE, "Atualização"),
#         (ACTION_DELETE, "Exclusão"),
#     ]

#     item_title = models.CharField(
#         verbose_name="Título Item Acervo",
#         null=False,
#         blank=False,
#     )
#     item_code = models.CharField(
#         verbose_name="Código do Item",
#         max_length=10,
#         null=False,
#         blank=False,
#     )
#     action = models.CharField(
#         max_length=10,
#         choices=ACTION_CHOICES,
#         verbose_name="Ação",
#         default=None,
#         null=True,
#     )
#     field_changed = models.CharField(
#         max_length=50, verbose_name="Campo Alterado", blank=True, null=True
#     )
#     previous_value = models.CharField(
#         max_length=255, verbose_name="Valor Anterior", blank=True, null=True
#     )
#     new_value = models.CharField(
#         max_length=255, verbose_name="Novo Valor", blank=True, null=True
#     )
#     changed_at = models.DateTimeField(verbose_name="Data da Alteração", default=now)
#     changed_by = models.CharField(
#         max_length=150,
#         verbose_name="Responsável pela Alteração",
#         blank=False,
#         null=False,
#     )

#     def action_display(self):
#         return dict(self.ACTION_CHOICES).get(self.action, "Desconhecido")

#     def field_changed_display(self):
#         if self.field_changed == "availability":
#             return "Disponibilidade"
#         elif self.field_changed == "preservation":
#             return "Estado de Conservação"
#         else:
#             return self.field_changed or "Desconhecido"

#     def availability_display(self):
#         if self.item:
#             return self.item.ESTADO_DISPONIVEL.get(
#                 self.item.availability, "Desconhecido"
#             )
#         return "Desconhecido"

#     def preservation_display(self):
#         if self.item:
#             return self.item.ESTADO_CONSEVACAO.get(
#                 self.item.preservation, "Desconhecido"
#             )
#         return "Desconhecido"

#     class Meta:
#         ordering = ["-changed_at"]
#         verbose_name = "Log de Alteração de Item"
#         verbose_name_plural = "Logs de Alteração de Item"

#     def __str__(self):
#         return f"{self.item} - {self.action} por {self.changed_by} em {self.changed_at}"






# collection_item/forms.py

def save(self, commit=True):
    # is_update = self.instance.pk is not None
    # previous_availability = None
    # previous_preservation = None
    # if is_update:
    #     old_item = CollectionItem.objects.get(pk=self.instance.pk)
    #     previous_availability = old_item.availability
    #     previous_preservation = old_item.preservation

    instance = super().save(commit=commit)

    # if is_update:
    #     # Registra alteração de disponibilidade
    #     if previous_availability != instance.availability:
    #         ItemStatusChange.objects.create(
    #             item=instance,
    #             action="update",
    #             field_changed="availability",
    #             previous_value=previous_availability,
    #             new_value=instance.availability,
    #             changed_at=timezone.now(),
    #             changed_by=self.user,
    #         )
    #         return instance
    #     # Registra alteração de preservação

    #     if previous_preservation != instance.preservation:
    #         ItemStatusChange.objects.create(
    #             item=instance,
    #             action="update",
    #             field_changed="preservation",
    #             previous_value=previous_preservation,
    #             new_value=instance.preservation,
    #             changed_at=timezone.now(),
    #             changed_by=self.user,
    #         )
    #         return instance

    return instance
