from django.db import models

# modelos

class Mascota(models.Model):
    numero_identificacion = models.IntegerField(unique= True)
    nombre = models.CharField(max_length = 100)
    especie = models.CharField(max_length = 50)
    raza = models.CharField(max_length = 50)
    fecha_nacimiento = models.DateField(null = True)
    duenno = models.CharField(max_length = 100)
    fecha_incorporacion = models.DateTimeField(null = True)

    def __str__(self):
        return f"Mascota: {self.nombre} - Especie: {self.especie} - Raza: {self.raza} - Dueño: {self.duenno} - Fecha de Incorporación: {self.fecha_incorporacion}"

class Doctor(models.Model):
    nombre = models.CharField(max_length = 100)
    especialidad = models.CharField(max_length = 100)
    email = models.EmailField()

    def __str__(self):
        return f"Doctor: {self.nombre} - Especialidad: {self.especialidad} - Email: {self.email}"

class Cita(models.Model):
    mascota = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    fecha_hora = models.DateTimeField()
    motivo = models.CharField(max_length = 200)

    def __str__(self):
        return f"Cita: {self.mascota} con Dr. {self.doctor} el {self.fecha_hora} - Motivo: {self.motivo}"


