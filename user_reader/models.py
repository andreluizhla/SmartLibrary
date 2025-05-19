from django.db import models

class User(models.Model):
    name = models.CharField(verbose_name="Nome Completo", max_length=100, null=False, blank=False)
    cpf = models.IntegerField(verbose_name="CPF", null=False, blank=False)
    cgm = models.IntegerField(verbose_name="CGM", null=False, blank=False)
    email = models.EmailField(verbose_name="E-mail", max_length=200, null=False, blank=False)
    phone = models.PositiveIntegerField(verbose_name="Telefone")
