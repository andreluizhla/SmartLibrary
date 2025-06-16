from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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
        messages.success(self.request, "Leitor cadastrado com sucesso!")
        return response


class UserReaderUpdateView(UpdateView):
    model = User
    fields = ["name", "cpf", "cgm", "email", "phone", "password"]
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Leitor atualizado com sucesso!")
        return response


class UserReaderDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Leitor excluido com sucesso!")
        return response


def home_page(request):
    return render(request, "user_reader/home_page.html")
