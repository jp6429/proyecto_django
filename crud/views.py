from django.shortcuts import render, HttpResponse, redirect, reverse  

from .models import *
from .forms import *

# Create your views here.
def root(request):
    return redirect('mascots/')

def mascots_list(request):
    context = {'mascotas': Mascot.objects.all()}
    return render(request,'crud/mascotas.html',context)

def mascots_new(request):
    if request.method == 'POST':
        form = MascotForm(request.POST, request.FILES)
        if form.is_valid():
            idMascot = form.cleaned_data.get('idMascot')
            name = form.cleaned_data.get('name')
            mascotType = form.cleaned_data.get('mascotType')
            breed = form.cleaned_data.get('breed')
            gender = form.cleaned_data.get('gender')
            image = form.cleaned_data.get('image')
            obj = Mascot.objects.create(
                idMascot = idMascot,
                name = name,
                mascotType = mascotType,
                breed = breed,
                gender = gender,
                image = image
            )
            obj.save()
            return redirect(reverse('mascots') + '?OK')
        else:
            return redirect(reverse('mascots') + '?FAIL')
    else:    
        form = MascotForm
    return render(request,'crud/mascotas-new.html',{'form':form})

def mascots_update(request,mascotas_id):
    try:
        mascotas = Mascot.objects.get(idMascot = mascotas_id)
        form = MascotForm(instance=mascotas)

        if request.method == 'POST':
            form = MascotForm(request.POST, request.FILES, instance=mascotas)
            if form.is_valid():
                form.save()
                return redirect(reverse('mascots') + '?UPDATED')
            else:
                return redirect(reverse('mascots-edit') + mascotas_id) 

        context = {'form':form}
        return render(request,'crud/mascotas-edit.html',context)
    except:
        return redirect(reverse('mascotas') + '?NO_EXISTS')

def mascots_detail(request,mascotas_id):
    try:
        mascotas = Mascot.objects.get(idMascot=mascotas_id)
        if mascotas:
            context = {'mascotas': mascotas }
            return render(request,'crud/mascotas-detail.html',context)
        else:
            return redirect(reverse('mascots') + '?NO_EXIST')
    except:
        return redirect(reverse('mascots') + '?NO_EXIST')

def mascots_delete(request,mascotas_id):
    try:
        mascotas = Mascot.objects.get(idMascot=mascotas_id)
        mascotas.delete()
        return redirect(reverse('mascots') + '?DELETED')
    except:
        return redirect(reverse('mascots') + '?FAIL')

def mascots_by_mascotType(request, mascotType):
    try:
        mascotas = Mascot.objects.filter(mascotType=mascotType)
        if mascotas:
            context = {'mascotas': mascotas }
            return render(request,'crud/mascotas.html',context)
        else:
            return redirect(reverse('mascots') + '?FAIL')
    except:
        return redirect(reverse('mascots') + '?FAIL')

def mascots_by_gender(request, gender):
    try:
        mascotas = Mascot.objects.filter(gender=gender)
        if mascotas:
            context = {'mascotas':mascotas}
            return render(request,'crud/mascotas.html',context)
        else:
            return redirect(reverse('mascots') + '?FAIL')
    except:
        return redirect(reverse('mascots') + '?FAIL')

def contact(request):
    data = {
        'form' : ContactForm()
    }

    if request.method == 'POST':
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado."
        else:
            data["form"] = formulario

    return render(request,'core/contacto.html', data)