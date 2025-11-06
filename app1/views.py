from django.shortcuts import render, redirect, get_object_or_404
from app1.forms import *
from app1.models import Mascota, Doctor, Cita
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "app1/index.html")


def crear_mascota(request):
    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("crear_mascota")
    else:
        form = MascotaForm()
    return render(request, "app1/crear_mascota.html", {"form": form})

def lista_mascotas(request):
    query = request.GET.get('q', '')
    if len (query) > 0:
        mascotas = Mascota.objects.filter (nombre__icontains = query).order_by ('-fecha_incorporacion')
    else:
        mascotas = Mascota.objects.all().order_by ('-fecha_incorporacion')
    return render(request, "app1/lista_mascotas.html", {"mascotas": mascotas, "query": query})

def crear_doctor(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("crear_doctor")
    else:
        form = DoctorForm()
    return render(request, "app1/crear_doctor.html", {"form": form})

def lista_doctores(request):
    query = request.GET.get('q', '')
    if len (query) > 0:
        doctores = Doctor.objects.filter (nombre__icontains = query).order_by ('nombre')
    else:
        doctores = Doctor.objects.all().order_by ('nombre')
    return render(request, "app1/lista_doctores.html", {"doctores": doctores, "query": query})

def crear_cita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("crear_cita")
    else:
        form = CitaForm()
    return render(request, "app1/crear_cita.html", {"form": form})

def lista_citas(request):
    query = request.GET.get('q', '')
    if len (query) > 0:
        citas = Cita.objects.filter (mascota__icontains = query).order_by ('-fecha_hora')
    else:
        citas = Cita.objects.all().order_by ('-fecha_hora')
    return render(request, "app1/lista_citas.html", {"citas": citas, "query": query})

def eliminar_mascota(request, numero_identificacion):
    mascota = get_object_or_404(Mascota, numero_identificacion=numero_identificacion)
    mascota.delete()
    messages.success(request, "Mascota eliminada correctamente.")
    return redirect("lista_mascotas")

def eliminar_doctor(request, nombre):
    doctor = get_object_or_404(Doctor, nombre=nombre)
    doctor.delete()
    messages.success(request, "Doctor eliminado correctamente.")
    return redirect("lista_doctores")

def eliminar_cita(request, mascota):
    cita = get_object_or_404(Cita, mascota=mascota)
    cita.delete()
    messages.success(request, "Cita eliminada correctamente.")
    return redirect("lista_citas")

def actualizar_mascota(request, numero_identificacion):
    mascota = get_object_or_404(Mascota, numero_identificacion=numero_identificacion)
    if request.method == "POST":
        form = MascotaEditForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            messages.success(request, "Mascota actualizada correctamente.")
            return redirect("lista_mascotas")
    else:
        form = MascotaEditForm(instance=mascota)
    return render(request, "app1/crear_mascota.html", {"form": form, 'edicion': True})

def actualizar_doctor(request, nombre):
    doctor = get_object_or_404(Doctor, nombre=nombre)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor actualizado correctamente.")
            return redirect("lista_doctores")
    else:
        form = DoctorForm(instance=doctor)
    return render(request, "app1/crear_doctor.html", {"form": form, 'edicion': True})

def actualizar_cita(request, mascota):
    cita = get_object_or_404(Cita, mascota=mascota)
    if request.method == "POST":
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request, "Cita actualizada correctamente.")
            return redirect("lista_citas")
    else:
        form = CitaForm(instance=cita)
    return render(request, "app1/crear_cita.html", {"form": form, 'edicion': True})