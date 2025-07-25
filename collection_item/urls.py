from django.urls import path
from .views import (
    # CollectionItem
    CollectionItemCreateView,
    CollectionItemDeleteView,
    CollectionItemListView,
    CollectionItemUpdateView,
    CollectionItemDetailView,
    # ItemHistory
    # ItemHistoryView,
    # DelayPolicy
    DelayPolicyListView,
    DelayPolicyCreateView,
    DelayPolicyUpdateView,
    DelayPolicyDeleteView,
    DelayPolicyDetail,
)

urlpatterns = [
    # URLS do CollectionItem
    path(
        "",
        CollectionItemListView.as_view(),
        name="collection_item_list",
    ),
    # path("<int:type>/", CollectionItemListView.as_view(), name="collection_item_list"),
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
    # path("update/<str:pk>", BookUpdateView.as_view(), name="book_update"),
    # path("update/<str:pk>", EquipmentUpdateView.as_view(), name="equipment_update"),
    path(
        "delete/<str:pk>",
        CollectionItemDeleteView.as_view(),
        name="collection_item_delete",
    ),
    path(
        "detail/<str:pk>",
        CollectionItemDetailView.as_view(),
        name="collection_item_detail",
    ),
    # URLS do ItemHistory
    # path(
    #     "history",
    #     ItemHistoryView.as_view(),
    #     name="collection_item_history",
    # ),
    # URLS do DelayPolicy
    path(
        "delay-policy",
        DelayPolicyListView.as_view(),
        name="delay_policy_list",
    ),
    path(
        "delay-policy/create",
        DelayPolicyCreateView.as_view(),
        name="delay_policy_create",
    ),
    path(
        "delay-policy/update/<str:pk>",
        DelayPolicyUpdateView.as_view(),
        name="delay_policy_update",
    ),
    path(
        "delay-policy/delete/<str:pk>",
        DelayPolicyDeleteView.as_view(),
        name="delay_policy_delete",
    ),
    path(
        "delay-policy/detail/<str:pk>",
        DelayPolicyDetail.as_view(),
        name="delay_policy_detail",
    ),
]
