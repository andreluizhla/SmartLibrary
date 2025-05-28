from django.views.generic import ListView, CreateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseForbidden

from .form import CollectionItemForm
from .models import CollectionItem


class CollectionItemListView(ListView):
    model = CollectionItem


class CollectionItemCreateView(CreateView):
    model = CollectionItem
    form_class = CollectionItemForm
    template_name = "collection_item/collectionitem_form.html"
    # fields = ["title", "id_code", "preservation", "availability"]
    success_url = reverse_lazy("collection_item_list")


class CollectionItemDeleteView(DeleteView):
    model = CollectionItem
    success_url = reverse_lazy("collection_item_list")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.availability != "Disponível":
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)
