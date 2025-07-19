from django.urls import path
from .views import (
    # CollectionItem
    CollectionItemCreateView,
    # collection_item_create_view,
    CollectionItemDeleteView,
    CollectionItemListView,
    CollectionItemUpdateView,
    BookListView,
    EquipmentListView,
    # ItemHistory
    # ItemHistoryView,
    # DelayPolicy
    DelayPolicyListView,
    DelayPolicyCreateView,
    DelayPolicyUpdateView,
    DelayPolicyDeleteView,
)

urlpatterns = [
    # URLS do CollectionItem
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
        "book",
        BookListView.as_view(),
        name="book_list",
    ),
    path(
        "equipment",
        EquipmentListView.as_view(),
        name="equipment_list",
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
    # # URLS do Work
    # path(
    #     "work",
    #     CollectionItemListView.as_view(),
    #     name="work_list",
    # ),
    # path(
    #     "work/create",
    #     CollectionItemCreateView.as_view(),
    #     name="work_create",
    # ),
    # path(
    #     "work/update/<int:pk>",
    #     CollectionItemUpdateView.as_view(),
    #     name="work_update",
    # ),
    # path(
    #     "work/delete/<int:pk>",
    #     CollectionItemDeleteView.as_view(),
    #     name="work_delete",
    # ),
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
]
