from django.urls import path
from app1.views import crear_doctor, index, crear_mascota, lista_mascotas, lista_doctores, crear_cita, lista_citas

urlpatterns = [
    path("", index, name="index"),
    path("mascotas/nuevo/", crear_mascota, name="crear_mascota"),
    path("mascotas/", lista_mascotas, name="lista_mascotas"),
    path("doctores/nuevo/", crear_doctor, name="crear_doctor"),
    path("doctores/", lista_doctores, name="lista_doctores"),
    path("citas/nuevo/", crear_cita, name="crear_cita"),
    path("citas/", lista_citas, name="lista_citas"),
]
