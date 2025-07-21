# Modelos
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
    DetailView,
)

# Métodos para deslogar, logar, autenticar e cadastro
from django.contrib.auth import views as auth_views, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Redirecionamento e renderização
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Exibir mensagens
from django.contrib import messages
from django.core.exceptions import PermissionDenied

# Modelos do APP User
from .forms import UserUpdateForm, UserRegistrationForm, UserNewPassword, UserLoginForm
from .models import User, UserChangeLog


@login_required
def home_page(request):
    return render(request, "user/home_page.html")


# Classe para permitir apenas usuários logados como Bibliotecário ou ADM
class LibrarianPermissionMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (
            not request.user.is_authenticated
            or request.user.type_user != User.BIBLIOTECARIO
            or not request.user.is_superuser
        ):
            messages.warning(
                request, "Acesso restrito a Bibliotecários e Administradores"
            )
            return HttpResponseRedirect(reverse_lazy("home_page"))
        return super().dispatch(request, *args, **kwargs)


class UserAccountView(LoginRequiredMixin, DetailView):
    template_name = "user/user_account.html"

    def get_object(self):
        return self.request.user


# CRUD do User:
class UserListView(LibrarianPermissionMixin, ListView):
    login_url = reverse_lazy("user_login")
    model = User
    # context_object_name = "selected_user_type"

    def get_queryset(self):
        self.selected_type = int(self.request.GET.get("user_type", 0))

        return User.objects.filter(type_user=self.selected_type)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected_type"] = self.selected_type
        context["user_types_list"] = User.USERS_TYPES_LIST
        return context


class UserCreateView(LibrarianPermissionMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    # template_name = "user/register.html"
    success_url = reverse_lazy("user_list")
    login_url = reverse_lazy("user_login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response


class UserUpdateView(LibrarianPermissionMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "user/user_form.html"
    login_url = reverse_lazy("user_login")
    success_url = reverse_lazy("user_list")
    context_object_name = "user_being_edited"

    def form_valid(self, form):
        if form.has_changed():
            for field in form.changed_data:
                if field != "password":
                    UserChangeLog.objects.create(
                        user=self.object,
                        changed_by=self.request.user,
                        field_changed=field,
                        old_value=str(getattr(self.object, field)),
                        new_value=str(form.cleaned_data[field]),
                        change_type="update",
                    )
        messages.success(self.request, "Usuário atualizado com sucesso!")
        return super().form_valid(form)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    login_url = reverse_lazy("user_login")
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Usuário excluido com sucesso!")
        return response


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User


# Login User
class UserLogin(auth_views.LoginView):
    model = User
    form_class = UserLoginForm
    template_name = "user/login.html"


# Deslogar User
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy("home_page"))


# Alterar Senha
@login_required
def password(request):
    user_id = request.GET.get("user_id")
    user_being_edited = get_object_or_404(User, pk=user_id) if user_id else request.user

    if not (
        request.user.is_superuser
        or request.user.type_user == User.BIBLIOTECARIO
        or user_being_edited == request.user
    ):
        raise PermissionDenied

    if request.method == "POST":
        form = UserNewPassword(user_being_edited, request.POST)
        if form.is_valid():
            user = form.save()
            UserChangeLog.objects.create(
                user=user,
                changed_by=request.user,
                field_changed="password",
                old_value="",
                new_value="",
                change_type="password_change",
            )
            messages.success(request, "Senha alterada com sucesso!")
            return HttpResponseRedirect(reverse_lazy("user_list"))
    else:
        form = UserNewPassword(user=user_being_edited)

    return render(
        request,
        "user/password.html",
        {"form": form, "user_being_edited": user_being_edited},
    )
