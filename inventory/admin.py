from django.contrib import admin

from inventory.models import Stores

from inventory.models import Products

admin.site.register(Products)
admin.site.register(Stores)