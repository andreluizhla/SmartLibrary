from django import forms
from validadores.validar_info import validate_name
from django.utils import timezone
from .models import CollectionItem, Book, Equipment


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
            nome_usuario = (
                self.user.get_full_name() or self.user.username
            )
            # self.fields["responsible_person"].initial = nome_usuario



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["isbn", "title", "author", "publisher", "year_pub"]


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ["serial_number", "brand", "specifications"]
