from django.contrib import admin
from django.urls import path, include

from user.views import home_page

# Lista de URLs separados por apps

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # main page
    path("", home_page, name="home_page"),
    # user
    path("user/", include("user.urls")),
    # path("user/", user.views.UserListView.as_view(), name=user.views.UserListView.list_view_name),
    # collection_item
    path("collection-item/", include("collection_item.urls")),
    # collection
    path("collection/", include("collection.urls")),
]


# na app é recomendado criar um arquivo chamado "urls.py" para armazenar todas as urls do app
# por exemplo: na app USUARIO, tem os seguintes caminhos: login, list, create, entre outros...

# para criar as urls, é possível criar das seguintes maneiras:

# para Views de Classes
# path("caminho/", ViewClass.as_view(), name="nome")

# para Views de Funções:
# path("caminho/", view_function, name="nome")


# e então, nesse arquivo (SETUP/URLS.PY) é apenas incluído as urls do APP
# path("caminho principal de uma APP/", include(APP.urls))
