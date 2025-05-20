from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

from .forms import UserForm
from .models import User


class UserReaderListView(ListView):
    model = User


class UserReaderCreateView(CreateView):
    model = User
    fields = ["name", "cpf", "cgm", "email", "phone"]
    success_url = reverse_lazy("user_list")
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response
