from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    email = models.EmailField()
    nro_estudiante = models.IntegerField(unique = True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_nacimiento = models.DateField(null = True)

    def __str__(self):
        return f"Estudiante: {self.nombre} - Nro Estudiante: {self.nro_estudiante} "
