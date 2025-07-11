from django.db import models
from django.core.exceptions import ValidationError


class Collection(models.Model):
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
    collection_type = models.PositiveSmallIntegerField(
        choices=COLLECTION_TYPES,
        default=LIVRO,
        verbose_name="Tipo de Acervo",
        null=False,
        blank=False,
    )
    collection_id = models.CharField(primary_key=True, verbose_name="ID do Acervo")
    name = models.CharField(
        verbose_name="Título do Acervo", max_length=50, null=False, blank=False
    )
    author = models.CharField(
        verbose_name="Autor", max_length=50, null=False, blank=False
    )
    publisher = models.CharField(
        verbose_name="Editora", max_length=30, null=False, blank=False
    )
    year_pub = models.IntegerField(verbose_name="Ano", null=False, blank=False)
    responsible_person = models.CharField(
        verbose_name="Pessoa Responsável",
        max_length=100,
        null=False,
        blank=False,
    )

    def clean(self):
        if Collection.objects.filter(
            name=self.name,
            author=self.author,
            publisher=self.publisher,
            year_pub=self.year_pub,
        ).exists():
            raise ValidationError("Esse acervo já existe!")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def get_type_display(self):
        return dict(self.COLLECTION_TYPES).get(self.collection_type, "Desconhecido")
    
    class Meta:
        verbose_name = "Acervo"
        verbose_name_plural = "Acervos"
        ordering = ["collection_type", "name"]
