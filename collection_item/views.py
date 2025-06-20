from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import CollectionItemForm
from .models import CollectionItem, ItemStatusChange


class CollectionItemListView(ListView):
    model = CollectionItem


class CollectionItemCreateView(CreateView):
    model = CollectionItem
    form_class = CollectionItemForm
    template_name = "collection_item/collectionitem_form.html"
    success_url = reverse_lazy("collection_item_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Item de Acervo cadastrado com sucesso!")
        return response


class CollectionItemDeleteView(DeleteView):
    model = CollectionItem
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


class CollectionItemUpdateView(UpdateView):
    model = CollectionItem
    form_class = CollectionItemForm
    template_name = "collection_item/collectionitem_form.html"
    success_url = reverse_lazy("collection_item_list")

    def form_valid(self, form):
        # mensagem
        response = super().form_valid(form)
        messages.success(self.request, "Item de Acervo atualizado com sucesso!")
        # se responsável existe, coloca ele, senão, coloca Sistema
        responsavel = form.cleaned_data.get("responsavel", "Sistema")
        form.instance.responsavel_form_input = responsavel
        return super().form_valid(form), response


class ItemHistoryView(ListView):
    model = ItemStatusChange
    template_name = "collection_item/item_history.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["history"] = self.object.status_changes.all().order_by("-changed_at")
    #     return context
