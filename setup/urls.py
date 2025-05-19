from django.contrib import admin
from django.urls import path

from user_reader.views import UserReaderListView, UserReaderCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", UserReaderListView.as_view(), name="user_list"),
    path("create/", UserReaderCreateView.as_view(), name="user_create")
]
