from django.contrib import admin
from .models import Item, productCategory

admin.site.register(productCategory)
admin.site.register(Item)