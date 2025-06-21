from django.urls import path
from .views import UserCreateView, UserDeleteView, UserListView, UserUpdateView

urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path(
        "update/<str:pk>",
        UserUpdateView.as_view(),
        name="user_update",
    ),
    path(
        "delete/<str:pk>",
        UserDeleteView.as_view(),
        name="user_delete",
    ),
]
