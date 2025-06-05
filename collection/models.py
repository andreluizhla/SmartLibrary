from django.db import models
from django.core.exceptions import ValidationError


class Collection(models.Model):
    title = models.CharField(
        verbose_name="Título do Acervo", max_length=50, null=False, blank=False
    )
    author = models.CharField(
        verbose_name="Autor", max_length=50, null=False, blank=False
    )
    publisher = models.CharField(
        verbose_name="Editora", max_length=30, null=False, blank=False
    )
    year_pub = models.IntegerField(verbose_name="Ano", null=False, blank=False)

    def clean(self):
        if Collection.objects.filter(
            title=self.title,
            author=self.author,
            publisher=self.publisher,
            year_pub=self.year_pub,
        ).exists():
            raise ValidationError("Esse acervo já existe!")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
