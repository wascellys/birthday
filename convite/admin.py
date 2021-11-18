from django.contrib import admin

# Register your models here.
from convite.models import Evento, Convite

admin.site.register(Convite)
admin.site.register(Evento)