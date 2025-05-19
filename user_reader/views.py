from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import User

class UserReaderListView(ListView):
    model = User

class UserReaderCreateView(CreateView):
    model = User
    fields = ["name", "cpf", "cgm", "email", 'phone']
    success_url = reverse_lazy("user_list")