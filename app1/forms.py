from django import forms
from app1.models import Mascota, Doctor, Cita



class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['numero_identificacion', 'nombre', 'especie', 'raza', 'fecha_nacimiento', 'duenno', 'fecha_incorporacion']
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "numero_identificacion": forms.NumberInput(attrs={'class': 'form-control'}),
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "especie": forms.TextInput(attrs={'class': 'form-control'}),
            "raza": forms.TextInput(attrs={'class': 'form-control'}),
            "duenno": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_incorporacion": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'especialidad', 'email']
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "especialidad": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
        }

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['mascota', 'doctor', 'fecha_hora', 'motivo']
        widgets = {
            "mascota": forms.TextInput(attrs={'class': 'form-control'}),
            "doctor": forms.TextInput(attrs={'class': 'form-control'}),
            "fecha_hora": forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            "motivo": forms.TextInput(attrs={'class': 'form-control'}),
        }

class MascotaEditForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'fecha_nacimiento', 'duenno']
        widgets = {
            "fecha_nacimiento": forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "especie": forms.TextInput(attrs={'class': 'form-control'}),
            "raza": forms.TextInput(attrs={'class': 'form-control'}),
            "duenno": forms.TextInput(attrs={'class': 'form-control'}),
            
        }

