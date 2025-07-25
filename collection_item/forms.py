from django import forms
from django.core.exceptions import ValidationError
from validadores.validar_info import validate_name
from django.utils import timezone
from .models import CollectionItem, Book, Equipment, DelayPolicy
from user.models import User


class CollectionItemForm(forms.ModelForm):
    class Meta:
        model = CollectionItem
        fields = "__all__"

    def clean(self):
        cleaned_data = super(CollectionItemForm, self).clean()
        preservation = self.cleaned_data.get("preservation")
        availability = self.cleaned_data.get("availability")
        # responsible_person = self.cleaned_data.get("responsible_person")

        if (
            availability == CollectionItem.EMPRESTADO
            and preservation == CollectionItem.DANIFICADO
        ):
            self.add_error(
                "availability", "Não é possível emprestar estando Danificado"
            )

        # if not responsible_person:
        #     responsible_person = "Sistema"

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            pass
            # self.fields[""].disabled = True
        elif self.user:
            nome_usuario = self.user.get_full_name() or self.user.username
            # self.fields["responsible_person"].initial = nome_usuario


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["isbn", "title", "author", "publisher", "year_pub"]


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ["serial_number", "brand", "specifications"]


class DelayPolicyForm(forms.ModelForm):
    class Meta:
        model = DelayPolicy
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields["type_item"].disabled = True

    def clean(self):
        cleaned_data = super().clean()
        type_user = cleaned_data.get("type_user")
        type_item = cleaned_data.get("type_item")

        # Se estivermos atualizando um registro existente
        if self.instance.pk:
            # Verifica se existe outra política com os mesmos type_user e type_item, excluindo a atual
            if (
                DelayPolicy.objects.filter(type_user=type_user, type_item=type_item)
                .exclude(pk=self.instance.pk)
                .exists()
            ):
                raise ValidationError(
                    "Já existe uma política para este tipo de usuário (%(user_type)s) e item (%(item_type)s).",
                    params={
                        "user_type": self.instance.get_type_user_display(),
                        "item_type": self.instance.get_type_item_display(),
                    },
                    code="duplicate_policy",
                )
        else:
            # Para criação de novo registro
            if DelayPolicy.objects.filter(
                type_user=type_user, type_item=type_item
            ).exists():
                raise ValidationError(
                    "Já existe uma política para este tipo de usuário (%(user_type)s) e item (%(item_type)s).",
                    params={
                        "user_type": dict(User.USERS_TYPES_LIST).get(
                            type_user, "Desconhecido"
                        ),
                        "item_type": dict(CollectionItem.COLLECTION_TYPES).get(
                            type_item, "Desconhecido"
                        ),
                    },
                    code="duplicate_policy",
                )

        return cleaned_data
