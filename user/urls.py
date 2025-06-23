from django.urls import path
from .views import (
    # UserCreateView,
    UserDeleteView,
    UserListView,
    UserUpdateView,
    UserLogin,
    user_logout,
    user_account,
    register,
)

urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
    path("account/", user_account, name="user_account"),
    # path("create/", UserCreateView.as_view(), name="user_create"),
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
    path(
        "login",
        UserLogin.as_view(),
        name="user_login",
    ),
    path("logout", user_logout, name="user_logout"),
    path("register", register, name="user_register"),
]
