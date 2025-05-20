from django import forms
from .models import User
import re


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "cpf", "cgm", "email", "phone"]
