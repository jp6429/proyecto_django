from django import forms
from django.forms import ModelForm
from .models import *

class MascotForm(ModelForm):
    class Meta:
        model = Mascot
        fields = [
            'idMascot',
            'name',
            'mascotType',
            'breed',
            'gender',
            'image'
        ]
        labels = {
            'idMascot':'ID',
            'name':'Nombre',
            'mascotType':'Tipo de Mascota',
            'breed':'Raza de Mascota',
            'gender':'Genero de Mascota',
            'image':'Imagen'
        }
        widgets = {
            'idMascot':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mascotType':forms.Select(attrs={'class':'form-control'}),
            'breed':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class MascotTypeForm(ModelForm):
    pass

class GenderForm(ModelForm):
    pass

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'rut',
            'nombre',
            'apellido',
            'email',
            'comentario'
        ]
        labels = {
            'rut':'Rut de Contacto',
            'nombre':'Nombre de Contacto',
            'apellido':'Apellido de Contacto',
            'email':'Email de Contacto',
            'comentario':'Comentario'
        }
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'comentario':forms.Textarea(attrs={'class':'form-control'}),
        }