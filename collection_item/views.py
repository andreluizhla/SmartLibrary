from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    View,
    DetailView,
)
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CollectionItemForm, BookForm, EquipmentForm, DelayPolicyForm
from .models import CollectionItem, DelayPolicy, Equipment, Book
from user.views import LibrarianPermissionMixin
from user.models import User


class CollectionItemDetailView(LibrarianPermissionMixin, DetailView):
    model = CollectionItem
    context_object_name = "item"
    template_name = "collection_item/collectionitem_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.object

        # Carrega o objeto específico (Book ou Equipment)
        if item.type == CollectionItem.LIVRO:
            context["specific_item"] = Book.objects.get(pk=item.pk)
        else:
            context["specific_item"] = Equipment.objects.get(pk=item.pk)

        # Filtra políticas por tipo de item
        context["delaypolicy_list"] = DelayPolicy.objects.filter(type_item=item.type)

        return context


# CRUD CollectionList
class CollectionItemListView(LoginRequiredMixin, ListView):
    template_name = "collection_item/collectionitem_list.html"
    context_object_name = "items_list"
    # paginate_by=2

    def get_queryset(self):
        self.selected_type = int(self.request.GET.get("type", 0))

        if self.selected_type == CollectionItem.LIVRO:
            return Book.objects.all()
        else:
            return Equipment.objects.filter(type=self.selected_type)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["collection_types"] = CollectionItem.COLLECTION_TYPES
        context["selected_type"] = self.selected_type
        return context


class CollectionItemCreateView(LibrarianPermissionMixin, View):
    template_name = "collection_item/collectionitem_form.html"
    success_url = reverse_lazy("collection_item_list")

    def get(self, request, *args, **kwargs):
        context = {
            "item_form": CollectionItemForm(user=request.user),
            "book_form": BookForm(),
            "equipment_form": EquipmentForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        item_form = CollectionItemForm(request.POST, user=request.user)
        tipo = int(request.POST.get("type", -1))
        print(tipo)

        if tipo == CollectionItem.LIVRO:
            child_form = BookForm(request.POST)
            other_form = EquipmentForm()
            for field in other_form.fields.values():
                field.required = False
        else:
            child_form = EquipmentForm(request.POST)
            other_form = BookForm()
            for field in other_form.fields.values():
                field.required = False

        if item_form.is_valid() and child_form.is_valid():
            item = item_form.save(commit=False)
            tipo = int(request.POST.get("type", 0))
            item.type = tipo
            item.save()

            child = child_form.save(commit=False)
            child.pk = item.pk
            child.type = tipo
            child.save()

            messages.success(request, "Item de Acervo cadastrado com sucesso!")
            return redirect(self.success_url)
        else:
            messages.error(
                request, "Erro ao cadastrar! Por favor, verifique os campos."
            )
            context = {
                "item_form": item_form,
                "book_form": (
                    BookForm(request.POST)
                    if tipo == CollectionItem.LIVRO
                    else BookForm()
                ),
                "equipment_form": (
                    EquipmentForm(request.POST)
                    if tipo != CollectionItem.LIVRO
                    else EquipmentForm()
                ),
            }
            return render(request, self.template_name, context)


class CollectionItemUpdateView(LibrarianPermissionMixin, UpdateView):
    template_name = "collection_item/collectionitem_form.html"
    fields = "__all__"
    success_url = reverse_lazy("collection_item_list")

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        try:
            # Tenta encontrar como Book primeiro
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            try:
                # Se não encontrar como Book, tenta como Equipment
                return Equipment.objects.get(pk=pk)
            except Equipment.DoesNotExist:
                # Se não encontrar em nenhum, retorna 404
                messages.error("Item não encontrado")
                return redirect(reverse_lazy("collection_item_list"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()

        if isinstance(obj, Book):
            context["item_form"] = CollectionItemForm(
                instance=obj, user=self.request.user
            )
            context["book_form"] = BookForm(instance=obj)
            context["equipment_form"] = EquipmentForm()
        else:
            context["item_form"] = CollectionItemForm(
                instance=obj, user=self.request.user
            )
            context["book_form"] = BookForm()
            context["equipment_form"] = EquipmentForm(instance=obj)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        item_form = CollectionItemForm(
            request.POST, instance=self.object, user=request.user
        )

        if isinstance(self.object, Book):
            child_form = BookForm(request.POST, instance=self.object)
            other_form = EquipmentForm()
        else:
            child_form = EquipmentForm(request.POST, instance=self.object)
            other_form = BookForm()

        # Torna os campos do outro formulário não obrigatórios
        for field in other_form.fields.values():
            field.required = False

        if item_form.is_valid() and child_form.is_valid():
            item = item_form.save(commit=False)
            item.save()

            child = child_form.save(commit=False)
            child.pk = item.pk
            child.save()

            messages.success(request, "Item de Acervo atualizado com sucesso!")
            return redirect(self.success_url)
        else:
            messages.error(
                request, "Erro ao atualizar! Por favor, verifique os campos."
            )
            context = self.get_context_data()
            context["item_form"] = item_form
            if isinstance(self.object, Book):
                context["book_form"] = child_form
            else:
                context["equipment_form"] = child_form
            return render(request, self.template_name, context)


class CollectionItemDeleteView(LibrarianPermissionMixin, DeleteView):
    model = CollectionItem
    template_name = "collection_item/collectionitem_confirm_delete.html"
    success_url = reverse_lazy("collection_item_list")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if (
            self.object.availability == "Emprestado"
            or self.object.availability == "Reservado"
        ):
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Item de Acervo excluido com sucesso!")
        return response


# # ItemHistory View
# class ItemHistoryView(LibrarianPermissionMixin, ListView):
#     model = ItemStatusChange
#     template_name = "collection_item/item_history.html"


# CRUD do DelayPolicy:
class DelayPolicyListView(LibrarianPermissionMixin, ListView):
    model = DelayPolicy
    template_name = "delay_policy/delaypolicy_list.html"
    
    def get_queryset(self):
        self.selected_type_user = int(self.request.GET.get("user", 0))
        
        return DelayPolicy.objects.filter(type_user=self.selected_type_user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["types_user_list"] = DelayPolicy.TIPOS_USUARIOS
        context["selected_type_user"] = self.selected_type_user
        return context


class DelayPolicyCreateView(LibrarianPermissionMixin, CreateView):
    form_class = DelayPolicyForm
    template_name = "delay_policy/delaypolicy_form.html"
    success_url = reverse_lazy("delay_policy_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Política de Atraso cadastrada com sucesso!")
        return response


class DelayPolicyUpdateView(LibrarianPermissionMixin, UpdateView):
    model = DelayPolicy
    form_class = DelayPolicyForm
    template_name = "delay_policy/delaypolicy_form.html"
    success_url = reverse_lazy("delay_policy_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Política de Atraso atualizada com sucesso!")
        return response


class DelayPolicyDeleteView(LibrarianPermissionMixin, DeleteView):
    model = DelayPolicy
    template_name = "delay_policy/delaypolicy_confirm_delete.html"
    success_url = reverse_lazy("delay_policy_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Política de Atraso excluída com sucesso!")
        return response


class DelayPolicyDetail(LibrarianPermissionMixin, DetailView):
    model = DelayPolicy
    template_name = "delay_policy/delaypolicy_detail.html"
    context_object_name = "delaypolicy_item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        policy = self.object

        # Filtra os itens pelo tipo da política
        if policy.type_item == CollectionItem.LIVRO:
            context["book_list"] = Book.objects.all()
            context["equipment_list"] = []
        else:
            context["equipment_list"] = Equipment.objects.filter(type=policy.type_item)
            context["book_list"] = []

        return context
