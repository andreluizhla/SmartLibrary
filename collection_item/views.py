from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import CollectionItem


class CollectionItemListView(ListView):
    model = CollectionItem


class CollectionItemCreateView(CreateView):
    model = CollectionItem
    fields = ["title", "id_code", "preservation", "availability"]
    success_url = reverse_lazy("collection_item_list")

class CollectionItemDeleteView(DeleteView):
    model = CollectionItem
    success_url = "collection_item_list"
