from django import forms
from .models import User
import re


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "cpf", "cgm", "email", "phone", "password"]

    #     widget = {
    #         "password": forms.PasswordInput(
    #             attrs={
    #                 "type": "password",
    #             }
    #         )
    #     }

    # password = forms.CharField(
    #     label="Senha",
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Digite sua senha",
    #             "autocomplete": "new-password",
    #             "type": "password",
    #         }
    #     ),
    # )
