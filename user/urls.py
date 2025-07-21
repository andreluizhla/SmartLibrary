from django.urls import path
from .views import (
    UserCreateView,
    UserDeleteView,
    UserListView,
    UserUpdateView,
    UserDetailView,
    UserLogin,
    UserAccountView,
    user_logout,
    password,
)

urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
    path("account/", UserAccountView.as_view(), name="user_account"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path(
        "update/<str:pk>",
        UserUpdateView.as_view(),
        name="user_update",
    ),
    path("detail/<str:pk>", UserDetailView.as_view(), name="user_detail"),
    path(
        "password/",
        password,
        name="user_password",
    ),
    path(
        "delete/<str:pk>",
        UserDeleteView.as_view(),
        name="user_delete",
    ),
    path(
        "login",
        UserLogin.as_view(),
        name="user_login",
    ),
    path("logout", user_logout, name="user_logout"),
]
