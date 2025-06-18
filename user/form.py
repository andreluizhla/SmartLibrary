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
                    (0, "Leitor"),
                    (1, "Funcionário"),
                    (2, "Bibliotecario"),
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

        if user_type == 0:
            if not cgm:
                self.add_error("cgm", "CGM é obrigatório para leitores")
        else:
            cleaned_data["cgm"] = None

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["type_user"].disabled = True
            self.fields["cpf"].disabled = True