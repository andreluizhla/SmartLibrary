from django import forms
from django.core.exceptions import ValidationError
from .models import Collection


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = "__all__"
