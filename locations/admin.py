

# Register your models here.
from django.contrib import admin
from .models import Escuela, Categoria, PuntoInteres

admin.site.register(Escuela)
admin.site.register(Categoria)
admin.site.register(PuntoInteres)