from django.shortcuts import render, redirect, reverse  

from .models import *
from .forms import *

# Create your views here.
def root(request):
    return redirect(mascotas_list)

def mascotas_list(request):
    context = {'mascotas':Mascot.objects.all()}
    return render(request,'crud/mascotas.html',context)

def mascotas_new(request):
    if request.method == 'POST':
        form = MascotForm(request.POST, request.FILES)
        if form.is_valid():
            idMascot = form.cleaned_data.get('idMascot')
            name = form.cleaned_data.get('name')
            mascotType = form.cleaned_data.get('mascotType')
            breed = form.cleaned_data.get('breed')
            vaccine = form.cleaned_data.get('vaccine')
            image = form.cleaned_data.get('image')
            obj = Mascot.objects.create(
                idMascot = idMascot,
                name = name,
                mascotType = mascotType,
                breed = breed,
                vaccine = vaccine,
                image = image
            )
            obj.save()
            return redirect(reverse('mascotas-list') + '?OK')
        else:
            return redirect(reverse('mascotas-list') + '?FAIL')
    else:    
        form = MascotForm()
    return render(request,'crud/mascotas_new.html',{'form':form})

def mascotas_detail(request,mascota_id):
    try:
        mascota = Mascot.objects.get(idMascot=mascota_id)
        if mascota:
            context = {'mascota': mascota }
            return render(request,'crud/mascotas_detail.html',context)
        else:
            return redirect(reverse('mascotas-list') + '?NO_EXIST')
    except:
        return redirect(reverse('mascotas-list') + '?NO_EXIST')

def mascotas_edit(request,mascota_id):
    try:
        mascota = Mascot.objects.get(idMascot=mascota_id)
        form = MascotForm(instance=mascota)

        if request.method == 'POST':
            form = MascotForm(request.POST, request.FILES, instance=mascota)
            if form.is_valid():
                form.save()
                return redirect(reverse('mascota-list') + '?UPDATED')
            else:
                return redirect(reverse('mascota-edit') + mascota_id)

        context = {'form':form}
        return render(request,'crud/mascotas_edit.html',context)
    except:
        return redirect(reverse('mascotas-list') + '?NO_EXIST')

def mascotas_delete(request,mascota_id):
    try:
        mascota = Mascot.objects.get(idMascot=mascota_id)
        mascota.delete()
        return redirect(reverse('mascotas-list') + '?DELETED')
    except:
        return redirect(reverse('mascotas-list') + '?FAIL')

def mascotas_by_mascotType(request, mascotType):
    try:
        mascotas = Mascot.objects.filter(mascotType=mascotType)
        if mascotas:
            context = {'mascotas': mascotas }
            return render(request,'crud/mascotas.html',context)
        else:
            return redirect(reverse('mascotas-list') + '?FAIL')
    except:
        return redirect(reverse('mascotas-list') + '?FAIL')