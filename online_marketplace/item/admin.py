from django.contrib import admin

from .models import Category, Item

admin.site.register(Category) # add new field in database
admin.site.register(Item)
