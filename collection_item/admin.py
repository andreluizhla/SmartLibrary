from django.contrib import admin

from .models import CollectionItem, ItemStatusChange

# Register your models here.
admin.site.register(CollectionItem)
admin.site.register(ItemStatusChange)
