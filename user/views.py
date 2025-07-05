# Modelos
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

# Métodos para deslogar, logar, autenticar e cadastro
from django.contrib.auth import views as auth_views, logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Redirecionamento e renderização
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


# Exibir mensagens
from django.contrib import messages
from django.core.exceptions import PermissionDenied

# Modelos do APP User
from .forms import UserUpdateForm, UserRegistrationForm, UserNewPassword, UserLoginForm
from .models import User


def home_page(request):
    return render(request, "user/home_page.html")


def user_account(request):
    if request.user.is_authenticated:
        return render(request, "user/user_account.html")
    else:
        return HttpResponseRedirect(reverse_lazy("user_list"))


# CRUD do User:
class UserListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("user_login")
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tipos"] = {0: "Leitor", 1: "Funcionário", 2: "Bibliotecário"}
        return context


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "user/register.html"
    success_url = reverse_lazy("user_list")
    login_url = reverse_lazy("user_login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response

    def dispatch(self, request, *args, **kwargs):
        if (
            not request.user.is_superuser
            or request.user.type_user != User.BIBLIOTECARIO
        ):
            messages.warning(
                request,
                "Atenção: Essa área é restria apenas para os Bilbiotecários ou Administradores",
            )
            return HttpResponseRedirect(reverse_lazy("home_page"))
        return super().dispatch(request, *args, **kwargs)


def password(request):
    context_object_name = "user_being_edited"
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

    return render(
        request,
        "user/password.html",
        {"form": form, "context_object_name": context_object_name},
    )


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "user/user_form.html"
    login_url = reverse_lazy("user_login")
    success_url = reverse_lazy("user_list")
    context_object_name = "user_being_edited"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário atualizado com sucesso!")
        return response

    def dispatch(self, request, *args, **kwargs):
        if (
            not request.user.is_superuser
            or request.user.type_user != User.BIBLIOTECARIO
        ):
            messages.warning(
                request,
                "Atenção: Essa área é restria apenas para os Bilbiotecários ou Administradores",
            )
            return HttpResponseRedirect(reverse_lazy("home_page"))
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    login_url = reverse_lazy("user_login")
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário excluido com sucesso!")
        return response


# Login User
class UserLogin(auth_views.LoginView):
    model = User
    form_class = UserLoginForm
    template_name = "user/login.html"


# Deslogar User
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("home_page"))


# Cadastro de User
@login_required()
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
