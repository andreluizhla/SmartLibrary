# Modelos
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

# Métodos para deslogar, logar, autenticar e cadastro
from django.contrib.auth import views, logout, login, authenticate


# Redirecionamento e renderização
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


# Exibir mensagens
from django.contrib import messages

# Modelos do APP User
from .forms import UserUpdateForm, UserRegistrationForm, UserNewPassword
from .models import User


def home_page(request):
    return render(request, "user/home_page.html")


def user_account(request):
    return render(request, "user/user_account.html")


# CRUD do User:
class UserListView(ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona conversão para template (opcional)
        context["tipos"] = {0: "Leitor", 1: "Funcionário", 2: "Bibliotecário"}
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "user/register.html"
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response


def password(request):
    if request.method == "POST":
        form = UserNewPassword(request.POST)
        username = request.POST.get("username")
        email = request.POST.get("email")
        novasenha = request.POST.get("novasenha")

        user = User.objects.get(username=username)
        user.set_password(novasenha)
        user.save()
        messages.success(request, "Senha alterada com sucesso!")
    else:

        form = UserNewPassword(user=request.user)
        # messages.success(request, "Dados errados")
        # return render(request, "user/password.html")

    return render(request, "user/password.html", {"form": form})


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
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


# Login User
class UserLogin(views.LoginView):
    model = User
    success_url = reverse_lazy("user_account")
    template_name = "user/login.html"


# Deslogar User
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("home_page"))


# Cadastro de User
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Autentica e loga o usuário
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("home_page")
    else:
        form = UserRegistrationForm()

    return render(request, "user/register.html", {"form": form})
