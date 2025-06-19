from django.contrib import admin
from django.urls import path

from user.views import (
    UserListView,
    UserCreateView,
    UserDeleteView,
    UserUpdateView,
    home_page,
)

from collection_item.views import (
    CollectionItemListView,
    CollectionItemCreateView,
    CollectionItemDeleteView,
    CollectionItemUpdateView,
    ItemHistoryView,
)

from collection.views import (
    CollectionListView,
    CollectionCreateView,
    CollectionUpdateView,
    CollectionDeleteView,
)

# Lista de URLs separados por apps

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # main page
    path("", home_page, name="home_page"),
    #
    # user_reader
    path("user/", UserListView.as_view(), name="user_list"),
    path("user/create/", UserCreateView.as_view(), name="user_create"),
    path(
        "user/update/<str:pk>",
        UserUpdateView.as_view(),
        name="user_update",
    ),
    path(
        "user/delete/<str:pk>",
        UserDeleteView.as_view(),
        name="user_delete",
    ),
    #
    # collection_item
    path(
        "collection-item/",
        CollectionItemListView.as_view(),
        name="collection_item_list",
    ),
    path(
        "collection-item/create",
        CollectionItemCreateView.as_view(),
        name="collection_item_create",
    ),
    path(
        "collection-item/update/<str:pk>",
        CollectionItemUpdateView.as_view(),
        name="collection_item_update",
    ),
    path(
        "collection-item/delete/<str:pk>",
        CollectionItemDeleteView.as_view(),
        name="collection_item_delete",
    ),
    path(
        "collection-item/history",
        ItemHistoryView.as_view(),
        name="collection_item_history",
    ),
    #
    # collection
    path("collection", CollectionListView.as_view(), name="collection_list"),
    path("collection/create", CollectionCreateView.as_view(), name="collection_create"),
    path(
        "collection/update/<str:pk>",
        CollectionUpdateView.as_view(),
        name="collection_update",
    ),
    path(
        "collection/delete/<str:pk>",
        CollectionDeleteView.as_view(),
        name="collection_delete",
    ),
]

# path("caminho/", view.as_view(), name="nome")
