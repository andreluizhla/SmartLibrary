from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import UserForm
from .models import User

# def home(request):
#     return render(request, )

class UserReaderListView(ListView):
    model = User


# def user_reader_create(request):
#     return render(request, "user_reader/user_form", {'form' : form})


class UserReaderCreateView(CreateView):
    model = User
    fields = ["name", "cpf", "cgm", "email", "phone", "password"]
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response
