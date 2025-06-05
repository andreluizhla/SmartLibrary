from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render

from .models import Collection


class CollectionListView(ListView):
    model = Collection


class CollectionCreateView(CreateView):
    model = Collection
    fields = ["title", "author", "year_pub", "publisher"]
    success_url = reverse_lazy("collection_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Acervo cadastrado com sucesso!")
        return response


class CollectionUpdateView(UpdateView):
    model = Collection
    fields = ["title", "author", "year_pub", "publisher"]
    success_url = reverse_lazy("collection_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Acervo atualizado com sucesso!")
        return response


class CollectionDeleteView(DeleteView):
    model = Collection
    success_url = reverse_lazy("collection_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Acervo excluido com sucesso!")
        return response
