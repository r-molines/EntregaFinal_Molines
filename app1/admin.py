from django.contrib import admin
from app1.models import *
# Register your models here.

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especie", "raza", "duenno", "fecha_nacimiento", "numero_identificacion")
    list_display_links = ("nombre", "especie")
    search_fields = ("nombre", "especie", "raza", "duenno")
    list_filter = ("especie", "raza", "duenno", "fecha_nacimiento")
    ordering = ("nombre", "fecha_nacimiento")
    readonly_fields = ("numero_identificacion",)