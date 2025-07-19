# Arquivo para autenticação personalizada por email ou CPF
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class EmailOrCPFBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Verifica se é email ou CPF
            if "@" in username:
                user = User.objects.get(email=username)
            else:
                # Remove possíveis máscaras do CPF
                cpf = "".join(filter(str.isdigit, username))
                user = User.objects.get(cpf=cpf)

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
