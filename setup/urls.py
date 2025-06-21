from django.contrib import admin
from django.urls import path, include

from user.views import home_page

# Lista de URLs separados por apps

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # main page
    path("", home_page, name="home_page"),
    #
    # user_reader
    path("user/", include("user.urls")),
    #
    # collection_item
    path("collection-item/", include("collection_item.urls")),
    #
    # collection
    path("collection/", include("collection.urls")),
]

# path("caminho/", view.as_view(), name="nome")
