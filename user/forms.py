from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
    AuthenticationForm,
)
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Login (Email ou CPF)")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is None or password is None:
            raise ValidationError("Por favor, preencha ambos os campos.")

        user = None
        try:
            # Verifica se é email ou CPF
            if "@" in username:
                user = authenticate(username=username, password=password)
            else:
                # Remove máscara do CPF se houver
                cpf = "".join(filter(str.isdigit, username))
                user = authenticate(username=cpf, password=password)

            if user is None:
                raise ValidationError(
                    "Credenciais inválidas. Por favor, tente novamente."
                )

            self.user_cache = user
        except Exception as e:
            if user is None:
                raise ValidationError(
                    "Credenciais inválidas. Por favor, tente novamente."
                )
            raise ValidationError(
                "Ocorreu um erro durante o login. Por favor, coloque um email ou CPF com senha."
            )

        return self.cleaned_data


class UserUpdateForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Permitir que bibliotecários alterem o tipo de usuário
        if self.instance.type_user == User.BIBLIOTECARIO or self.instance.is_superuser:
            self.fields["type_user"].disabled = False

        # Sempre bloquear CPF após criação
        if self.instance.pk:
            self.fields["cpf"].disabled = True

    class Meta:
        model = User
        fields = [
            "type_user",
            "username",
            "email",
            "password",
            "cpf",
            "phone",
            "cgm",
            "status",
        ]
        widgets = {
            "status": forms.Select(choices=User.STATUS_CHOICES),
        }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "type_user",
            "username",
            "email",
            "password1",
            "password2",
            "cpf",
            "phone",
            "cgm",
        ]

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get("type_user")
        cgm = cleaned_data.get("cgm")

        if user_type == User.LEITOR and not cgm:
            self.add_error("cgm", "CGM é obrigatório para leitores")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["type_user"].disabled = True
            self.fields["cpf"].disabled = True


class UserNewPassword(PasswordChangeForm):
    class Meta:
        model = User
        fields = "__all__"
