from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from validadores.validar_info import (
    validate_isbn,
    validate_fine_value,
    validate_upper_zero,
)

UserModel = get_user_model()
from user.models import User

# from collection.models import Collection


class CollectionItem(models.Model):
    LIVRO = 0
    NOTEBOOK = 1
    CHROMEBOOK = 2
    TABLET = 3
    COLLECTION_TYPES = [
        (LIVRO, "Livro"),
        (NOTEBOOK, "Notebook"),
        (CHROMEBOOK, "Chromebook"),
        (TABLET, "Tablet"),
    ]
    type = models.PositiveSmallIntegerField(
        choices=COLLECTION_TYPES,
        default=LIVRO,
        verbose_name="Tipo de Acervo",
        null=False,
        blank=False,
    )

    NOVO = 0
    BOM = 1
    REGULAR = 2
    RUIM = 3
    DANIFICADO = 4
    ESTADO_CONSEVACAO = {
        NOVO: "Novo",
        BOM: "Bom",
        REGULAR: "Regular",
        RUIM: "Ruim",
        DANIFICADO: "Danificado",
    }
    preservation = models.PositiveSmallIntegerField(
        verbose_name="Estado de Conservação",
        choices=ESTADO_CONSEVACAO,
        null=False,
        blank=False,
        default=NOVO,
    )

    DISPONIVEL = 0
    EMPRESTADO = 1
    RESERVADO = 2
    INATIVO = 3
    ESTADO_DISPONIVEL = {
        DISPONIVEL: "Disponível",
        EMPRESTADO: "Emprestado",
        RESERVADO: "Reservado",
        INATIVO: "Inativo",
    }
    availability = models.PositiveSmallIntegerField(
        verbose_name="Disponibilidade",
        choices=ESTADO_DISPONIVEL,
        null=False,
        blank=False,
        default=DISPONIVEL,
    )

    class Meta:
        verbose_name = "Item do Acervo"
        verbose_name_plural = "Itens do Acervo"
        ordering = ["type"]

    def preservation_display(self):
        return self.ESTADO_CONSEVACAO.get(self.preservation, "Desconhecido")

    def availability_display(self):
        return self.ESTADO_DISPONIVEL.get(self.availability, "Desconhecido")

    def get_type_display(self):
        return dict(self.COLLECTION_TYPES).get(self.type, "Desconhecido")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Book(CollectionItem):
    isbn = models.CharField(
        verbose_name="ISBN",
        max_length=13,
        help_text="Digite apenas números",
        validators=[validate_isbn],
    )
    title = models.CharField(verbose_name="Título da Obra", max_length=100)
    author = models.CharField(verbose_name="Autor da Obra", max_length=50)
    publisher = models.CharField(verbose_name="Editora da Obra", max_length=50)
    year_pub = models.IntegerField(verbose_name="Ano de Publicação")

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def isbn_display(self):
        isbn = self.isbn
        if isbn != 13:
            return isbn[:2] + "-" + isbn[2:5] + "-" + isbn[5:9] + "-" + isbn[9:]
        else:
            return (
                isbn[:3]
                + "-"
                + isbn[3:5]
                + "-"
                + isbn[5:10]
                + "-"
                + isbn[10:12]
                + "-"
                + isbn[12:]
            )


class Equipment(CollectionItem):
    serial_number = models.CharField(verbose_name="Número de Série", max_length=20)
    brand = models.CharField(verbose_name="Marca/Modelo", max_length=100)
    specifications = models.TextField(verbose_name="Especificações")

    class Meta:
        verbose_name = "Equipamento Digital"
        verbose_name_plural = "Equipamentos Digitais"
        ordering = ["brand", "serial_number"]


class DelayPolicy(models.Model):
    TIPOS_USUARIOS = {
        User.LEITOR: "Leitor",
        User.FUNCIONARIO: "Funcionário",
    }
    type_user = models.PositiveSmallIntegerField(
        verbose_name="Tipo de Usuário",
        choices=TIPOS_USUARIOS,
        default=User.LEITOR,
        null=False,
        blank=False,
    )
    type_item = models.PositiveSmallIntegerField(
        verbose_name="Tipo de Item",
        choices=CollectionItem.COLLECTION_TYPES,
        default=CollectionItem.LIVRO,
        null=False,
        blank=False,
    )
    max_days = models.PositiveIntegerField(
        verbose_name="Prazo maximo de emprestimo (em dias)",
        null=False,
        blank=False,
        help_text="Tempo máximo (em dias) que o usuário poderá permanecer com o Item antes de começar a receber a multa.",
        validators=[validate_upper_zero],
    )
    fine_value = models.DecimalField(
        verbose_name="Valor da multa (por dias)",
        null=False,
        blank=False,
        max_digits=10,
        decimal_places=2,
        help_text="O valor da multa é calculado com base no número de dias em que o item não foi devolvido, multiplicado pelo valor diário da multa.",
        validators=[validate_fine_value],
    )
    item_limits = models.PositiveIntegerField(
        verbose_name="Limite de itens simultâneos",
        null=False,
        blank=False,
        help_text="Limite de Itens que o usuário pode emprestar",
        validators=[validate_upper_zero],
    )
    delay_tolerance = models.PositiveIntegerField(
        verbose_name="Tolerância de atraso (Opcional)",
        null=True,
        blank=True,
        help_text="Tempo máximo (em dias) que o usuário pode permanecer com o item sem ser multado.",
    )

    class Meta:
        verbose_name = "Política de Multa e Atrazo"
        verbose_name_plural = "Políticas de Multas e Atrazos"
        ordering = ["type_user", "type_item"]

    def clean(self):
        super().clean()
        if DelayPolicy.objects.filter(
            type_user=self.type_user, type_item=self.type_item
        ).exists():
            raise ValidationError("Essa multa já existe!")

    def fine_value_formatted(self):
        return "R$ " + str(self.fine_value).replace(".", ",")

    def delay_tolerance_formatted(self):
        if self.delay_tolerance:
            return str(self.delay_tolerance) + " dias"

    # def max_days_display(value):
    #     return value + " Dias"
