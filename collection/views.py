# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from django.contrib import messages
# from django.shortcuts import render

# from django.contrib.auth.mixins import LoginRequiredMixin

# # from .models import Collection
# from .forms import CollectionForm

# from user.views import LibrarianPermissionMixin


# class CollectionListView(LoginRequiredMixin, ListView):
#     model = Collection


# class CollectionCreateView(LibrarianPermissionMixin, CreateView):
#     model = Collection
#     form_class = CollectionForm
#     template_name = "collection/collection_form.html"
#     success_url = reverse_lazy("collection_list")

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, "Acervo cadastrado com sucesso!")
#         return response


# class CollectionUpdateView(LibrarianPermissionMixin, UpdateView):
#     model = Collection
#     form_class = CollectionForm
#     template_name = "collection/collection_form.html"
#     success_url = reverse_lazy("collection_list")

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, "Acervo atualizado com sucesso!")
#         return response


# class CollectionDeleteView(LibrarianPermissionMixin, DeleteView):
#     model = Collection
#     success_url = reverse_lazy("collection_list")

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         messages.success(self.request, "Acervo excluido com sucesso!")
#         return response
