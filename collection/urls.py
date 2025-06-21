from django.urls import path
from .views import (
    CollectionCreateView,
    CollectionDeleteView,
    CollectionListView,
    CollectionUpdateView,
)

urlpatterns = [
    path("", CollectionListView.as_view(), name="collection_list"),
    path("create/", CollectionCreateView.as_view(), name="collection_create"),
    path(
        "update/<str:pk>",
        CollectionUpdateView.as_view(),
        name="collection_update",
    ),
    path(
        "delete/<str:pk>",
        CollectionDeleteView.as_view(),
        name="collection_delete",
    ),
]
