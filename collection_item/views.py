from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import CollectionItem


class CollectionItemListView(ListView):
    model = CollectionItem


class CollectionItemCreateView(CreateView):
    model = CollectionItem
    fields = ["title", "id_code", "preservation", "availability"]
    success_url = reverse_lazy("collection_item_list")
