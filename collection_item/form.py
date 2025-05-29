from django import forms
from .validators import id_code_validator
from .models import CollectionItem
import random


class CollectionItemForm(forms.ModelForm):
    ESTADO_CONSERVACAO = {
        "Bom": "Bom",
        "Regular": "Regular",
        "Ruim": "Ruim",
        "Danificado": "Danificado",
    }

    ESTADO_DISPONIVEL = {
        "Disponível": "Disponível",
        "Emprestado": "Emprestado",
        "Reservado": "Reservado",
    }

    id_code = forms.CharField(
        label="Código Identificador",
        max_length=10,
        validators=[id_code_validator],
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "pattern": "[0-9]{10}",
                "title": "Apenas 10 dígitos",
            }
        ),
    )

    preservation = forms.ChoiceField(
        label="Estado de Conservação",
        choices=ESTADO_CONSERVACAO.items(),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    availability = forms.ChoiceField(
        label="Disponibilidade",
        choices=ESTADO_DISPONIVEL.items(),
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    responsavel = forms.CharField(
        label="Nome do Responsável",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Seu nome completo"}
        ),
    )

    class Meta:
        model = CollectionItem
        fields = ["title", "id_code", "preservation", "availability"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Título da obra"}
            ),
            "entry_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date", "readonly": True}
            ),
        }
        labels = {
            "title": "Título da Obra",
        }

    def clean(self):
        cleaned_data = super(CollectionItemForm, self).clean()
        preservation = self.cleaned_data.get("preservation")
        availability = self.cleaned_data.get("availability")

        if availability == "Emprestado" and preservation == "Danificado":
            self.add_error(
                "availability", "Não é possível emprestar estando Danificado"
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["id_code"].disabled = True
        else:
            del self.fields["responsavel"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        responsavel = self.cleaned_data.get("responsavel", "Sistema")
        instance.responsavel_form_input = responsavel
        if commit:
            instance.save()
        return instance
