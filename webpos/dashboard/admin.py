from django.contrib import admin
from .models import Item, productCategory ,Order

admin.site.register(productCategory)
admin.site.register(Item)
admin.site.register(Order)