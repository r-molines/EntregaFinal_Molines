from django.urls import path
from app1.views import crear_doctor, index, crear_mascota, lista_mascotas, lista_doctores, crear_cita, lista_citas, eliminar_mascota, eliminar_doctor, eliminar_cita, actualizar_mascota, actualizar_doctor, actualizar_cita

urlpatterns = [
    path("", index, name="index"),
    path("mascotas/nuevo/", crear_mascota, name="crear_mascota"),
    path("mascotas/", lista_mascotas, name="lista_mascotas"),
    path("doctores/nuevo/", crear_doctor, name="crear_doctor"),
    path("doctores/", lista_doctores, name="lista_doctores"),
    path("citas/nuevo/", crear_cita, name="crear_cita"),
    path("citas/", lista_citas, name="lista_citas"),
    path("mascotas/eliminar/<int:numero_identificacion>/", eliminar_mascota, name="eliminar_mascota"),
    path("doctores/eliminar/<str:nombre>/", eliminar_doctor, name="eliminar_doctor"),
    path("citas/eliminar/<str:mascota>/", eliminar_cita, name="eliminar_cita"),
    path("mascotas/actualizar/<int:numero_identificacion>/", actualizar_mascota, name="actualizar_mascota"),
    path("doctores/actualizar/<str:nombre>/", actualizar_doctor, name="actualizar_doctor"),
    path("citas/actualizar/<str:mascota>/", actualizar_cita, name="actualizar_cita"),
]
