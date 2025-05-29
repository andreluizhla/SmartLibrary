from django.contrib import admin
from django.urls import path

from user_reader.views import UserReaderListView, UserReaderCreateView

from collection_item.views import (
    CollectionItemListView,
    CollectionItemCreateView,
    CollectionItemDeleteView,
    CollectionItemUpdateView,
    ItemHistoryView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", UserReaderListView.as_view(), name="user_list"),
    path("create/", UserReaderCreateView.as_view(), name="user_create"),
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
        "collection-item/delete/<str:pk>",
        CollectionItemDeleteView.as_view(),
        name="collection_item_delete",
    ),
    path(
        "collection-item/update/<str:pk>",
        CollectionItemUpdateView.as_view(),
        name="collection_item_update",
    ),
    path(
        "collection-item/history",
        ItemHistoryView.as_view(),
        name="collection_item_history",
    ),
]

# path("caminho/", view.as_view(), name="nome")
