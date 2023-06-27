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