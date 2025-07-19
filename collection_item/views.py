from django.views.generic import ListView, CreateView, DeleteView, UpdateView, View
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CollectionItemForm, BookForm, EquipmentForm
from .models import CollectionItem, DelayPolicy, Equipment, Book
from user.views import LibrarianPermissionMixin


# CRUD CollectionList
class CollectionItemListView(ListView):
    model = CollectionItem
    template_name = "collection_item/collection_item/collectionitem_list.html"


# class CollectionItemCreateView(LibrarianPermissionMixin, CreateView):
#     model = CollectionItem
#     form_class = CollectionItemForm
#     template_name = "collection_item/collection_item/collectionitem_form.html"
#     success_url = reverse_lazy("collection_item_list")


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "collection_item/book_list.html"

    def get_queryset(self):
        return Book.objects.all()


class EquipmentListView(LoginRequiredMixin, ListView):
    model = Equipment
    template_name = "collection_item/equipment_list.html"

    def get_queryset(self):
        return Equipment.objects.all()


class CollectionItemCreateView(LibrarianPermissionMixin, View):
    template_name = "collection_item/collection_item/collectionitem_form.html"
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
            item.save()

            child = child_form.save(commit=False)
            child.pk = item.pk
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

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     return response


class CollectionItemDeleteView(LibrarianPermissionMixin, DeleteView):
    model = CollectionItem
    template_name = "collection_item/collection_item/collectionitem_confirm_delete.html"
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


class CollectionItemUpdateView(LibrarianPermissionMixin, UpdateView):
    model = CollectionItem
    form_class = CollectionItemForm
    template_name = "collection_item/collectionitem_form.html"
    success_url = reverse_lazy("collection_item_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa o usuário à instância
        return super().form_valid(form)

    def form_valid(self, form):
        form.instance.responsavel_form_input = (
            self.request.user.username or self.request.user.get_full_name()
        )
        response = super().form_valid(form)
        messages.success(self.request, "Item de Acervo atualizado com sucesso!")
        # se responsável existe, coloca ele, senão, coloca Sistema
        responsavel = form.cleaned_data.get("responsavel", "Sistema")
        form.instance.responsavel_form_input = responsavel
        return response


# CRUD do Work:
# class WorkListView(LoginRequiredMixin, ListView):
#     model = Work
#     template_name = "collection_item/work_list.html"

# class WorkCreateView(LibrarianPermissionMixin, CreateView):
#     model = Work
#     fields = "__all__"
#     template_name = "collection_item/work_form.html"
#     success_url = reverse_lazy("work_list")

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, "Obra cadastrada com sucesso!")
#         return response

# class WorkUpdateView(LibrarianPermissionMixin, UpdateView):
#     model = Work
#     fields = "__all__"
#     template_name = "collection_item/work_form.html"
#     success_url = reverse_lazy("work_list")

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, "Obra atualizada com sucesso!")
#         return response

# class WorkDeleteView(LibrarianPermissionMixin, DeleteView):
#     model = Work
#     success_url = reverse_lazy("work_list")

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, "Obra excluída com sucesso!")
#         return response

# # ItemHistory View
# class ItemHistoryView(LibrarianPermissionMixin, ListView):
#     model = ItemStatusChange
#     template_name = "collection_item/item_history.html"


# CRUD do DelayPolicy:
class DelayPolicyListView(LibrarianPermissionMixin, ListView):
    model = DelayPolicy
    template_name = "collection_item/delay_policy/delaypolicy_list.html"


class DelayPolicyCreateView(LibrarianPermissionMixin, CreateView):
    model = DelayPolicy
    fields = "__all__"
    template_name = "collection_item/delay_policy/delaypolicy_form.html"
    success_url = reverse_lazy("delay_policy_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Política de Atraso cadastrada com sucesso!")
        return response


class DelayPolicyUpdateView(LibrarianPermissionMixin, UpdateView):
    model = DelayPolicy
    fields = "__all__"
    template_name = "collection_item/delay_policy/delaypolicy_form.html"
    success_url = reverse_lazy("delay_policy_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Política de Atraso atualizada com sucesso!")
        return response


class DelayPolicyDeleteView(LibrarianPermissionMixin, DeleteView):
    model = DelayPolicy
    template_name = "collection_item/delay_policy/delaypolicy_confirm_delete.html"
    success_url = reverse_lazy("delay_policy_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Política de Atraso excluída com sucesso!")
        return response
