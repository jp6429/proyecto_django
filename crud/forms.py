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
            'vaccine',
            'image'
        ]
        labels = {
            'idMascot':'ID',
            'name':'Nombre',
            'mascotType':'Tipo de Mascota',
            'breed':'Raza de Mascota',
            'vaccine':'Vacuna(s)',
            'image':'Imagen'
        }
        widgets = {
            'idMascot':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mascotType':forms.Select(attrs={'class':'form-control'}),
            'breed':forms.TextInput(attrs={'class':'form-control'}),
            'vaccine':forms.CheckboxSelectMultiple(),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class MascotTypeForm(ModelForm):
    pass

class VaccineForm(ModelForm):
    pass