from django.contrib import admin
from .models import Client,Vendor,Item,Order
from django.contrib.auth.models import Group

# admin.site.unregister(Group)

admin.site.register(Client)
admin.site.register(Vendor)
admin.site.register(Item)
admin.site.register(Order)