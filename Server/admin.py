from django.contrib import admin
from .models import Server, ServerList

# Register your models here.
admin.site.register(Server)
admin.site.register(ServerList)
