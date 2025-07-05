from django.urls import path
from .views import (
    CollectionItemCreateView,
    CollectionItemDeleteView,
    CollectionItemListView,
    CollectionItemUpdateView,
    ItemHistoryView,
    DelayPolicyListView,
)

urlpatterns = [
    path(
        "",
        CollectionItemListView.as_view(),
        name="collection_item_list",
    ),
    path(
        "create",
        CollectionItemCreateView.as_view(),
        name="collection_item_create",
    ),
    path(
        "update/<str:pk>",
        CollectionItemUpdateView.as_view(),
        name="collection_item_update",
    ),
    path(
        "delete/<str:pk>",
        CollectionItemDeleteView.as_view(),
        name="collection_item_delete",
    ),
    path(
        "history",
        ItemHistoryView.as_view(),
        name="collection_item_history",
    ),
    path(
        "delay-policy",
        DelayPolicyListView.as_view(),
        name="delay_policy_list",
    ),
]
