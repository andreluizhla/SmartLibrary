from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages

from .form import UserForm
from .models import User

# def home(request):
#     return render(request, )


class UserListView(ListView):
    model = User


# def user_reader_create(request):
#     return render(request, "user_reader/user_form", {'form' : form})


class UserCreateView(CreateView):
    model = User
    # fields = "__all__"
    form_class = UserForm
    template_name = "user/user_form.html"
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response


class UserUpdateView(UpdateView):
    model = User
    # fields = ["name", "cpf", "cgm", "email", "phone", "password"]
    form_class = UserForm
    template_name = "user/user_form.html"
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário atualizado com sucesso!")
        return response


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário excluido com sucesso!")
        return response


def home_page(request):
    return render(request, "user/home_page.html")
