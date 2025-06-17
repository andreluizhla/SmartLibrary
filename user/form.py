from django import forms
from .models import User
import re


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

        widgets = {
            "type_user": forms.Select(
                attrs={"onchange": "mostrarCamposUsuarios()"},
                choices=[
                    ("LEITOR", "Leitor"),
                    ("FUNCIONARIO", "Funcionário"),
                    ("BIBLIOTECARIO", "Bibliotecario"),
                ],
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite sua senha",
                    "autocomplete": "new-password",
                }
            ),
            "cgm": forms.TextInput(
                attrs={
                    "data-required-for": "LEITOR",
                    "class": "form-control",
                    "placeholder": "Entrada para Leitor",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get("type_user")
        cgm = cleaned_data.get("cgm")

        if user_type == "LEITOR":
            if not cgm:
                self.add_error("cgm", "CGM é obrigatório para leitores")
        else:
            cleaned_data["cgm"] = None

        return cleaned_data
