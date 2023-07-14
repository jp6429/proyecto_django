from django.shortcuts import render, HttpResponse, redirect, reverse  

from .models import *
from .forms import *

# Create your views here.
def root(request):
    if 'usuario' not in request.session:
        return redirect("/")

    #if request.session.usuario.rol == 'ADMIN':
    return redirect('mascots/')

def mascots_list(request):
    if 'usuario' not in request.session:
        return redirect("/")
    
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")

    context = {'mascotas': Mascot.objects.all()}
    return render(request,'crud/mascotas.html',context)

def mascots_new(request):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

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
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

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
        return redirect(reverse('mascots') + '?NO_EXISTS')

def mascots_detail(request,mascotas_id):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

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
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

    try:
        mascotas = Mascot.objects.get(idMascot=mascotas_id)
        mascotas.delete()
        return redirect(reverse('mascots') + '?DELETED')
    except:
        return redirect(reverse('mascots') + '?FAIL')

def mascots_by_mascotType(request, mascotType):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

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
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

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

def mascotsType_list(request):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

    context = {'mascotasTipo': MascotType.objects.all()}
    return render(request,'crud/mascotasType.html',context)

def mascotsType_new(request):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

    if request.method == 'POST':
        form = MascotTypeForm(request.POST, request.FILES)
        if form.is_valid():
            mascotType = form.cleaned_data.get('mascotType')
            obj = MascotType.objects.create(
                mascotType = mascotType,
            )
            obj.save()
            return redirect(reverse('mascotasType') + '?OK')
        else:
            return redirect(reverse('mascotasType') + '?FAIL')
    else:    
        form = MascotTypeForm
    return render(request,'crud/mascotasType-new.html',{'form':form})

def mascotsType_update(request,mascotasTipo_id):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

    try:
        mascotasTipo = MascotType.objects.get(id = mascotasTipo_id)
        form = MascotTypeForm(instance=mascotasTipo)

        if request.method == 'POST':
            form = MascotTypeForm(request.POST, request.FILES, instance=mascotasTipo)
            if form.is_valid():
                form.save()
                return redirect(reverse('mascotasType') + '?UPDATED')
            else:
                return redirect(reverse('mascotasType-edit') + mascotasTipo_id) 

        context = {'form':form}
        return render(request,'crud/mascotasType-edit.html',context)
    except:
        return redirect(reverse('mascotasTipo') + '?NO_EXISTS')

def mascotsType_detail(request,mascotasTipo_id):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

    try:
        mascotasTipo = MascotType.objects.get(id = mascotasTipo_id)
        if mascotasTipo:
            context = {'mascotasTipo': mascotasTipo }
            return render(request,'crud/mascotasType-detail.html',context)
        else:
            return redirect(reverse('mascotasType') + '?NO_EXIST')
    except:
        return redirect(reverse('mascotasType') + '?NO_EXIST')

def mascotsType_delete(request,mascotasTipo_id):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

    try:
        mascotasTipo = MascotType.objects.get(id=mascotasTipo_id)
        mascotasTipo.delete()
        return redirect(reverse('mascotasType') + '?DELETED')
    except:
        return redirect(reverse('mascotasType') + '?FAIL')

def gender_list(request):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

    context = {'genero': Gender.objects.all()}
    return render(request,'crud/genero.html',context)

def gender_new(request):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

    if request.method == 'POST':
        form = GenderForm(request.POST, request.FILES)
        if form.is_valid():
            gender = form.cleaned_data.get('gender')
            obj = Gender.objects.create(
                gender = gender,
            )
            obj.save()
            return redirect(reverse('genero') + '?OK')
        else:
            return redirect(reverse('genero') + '?FAIL')
    else:    
        form = GenderForm
    return render(request,'crud/genero-new.html',{'form':form})

def gender_update(request,genero_id):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

    try:
        genero = Gender.objects.get(id = genero_id)
        form = GenderForm(instance=genero)

        if request.method == 'POST':
            form = GenderForm(request.POST, request.FILES, instance=genero)
            if form.is_valid():
                form.save()
                return redirect(reverse('genero') + '?UPDATED')
            else:
                return redirect(reverse('genero-edit') + genero_id) 

        context = {'form':form}
        return render(request,'crud/genero-edit.html',context)
    except:
        return redirect(reverse('genero') + '?NO_EXISTS')

def gender_detail(request,genero_id):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

    try:
        genero = Gender.objects.get(id=genero_id)
        if genero:
            context = {'genero': genero }
            return render(request,'crud/genero-detail.html',context)
        else:
            return redirect(reverse('genero') + '?NO_EXIST')
    except:
        return redirect(reverse('genero') + '?NO_EXIST')

def gender_delete(request,genero_id):
    #if 'ADMIN' not in request.session.usuario.rol:
    #    return redirect("/")
    if 'usuario' not in request.session:
        return redirect("/")

    try:
        genero = MascotType.objects.get(id=genero_id)
        genero.delete()
        return redirect(reverse('genero') + '?DELETED')
    except:
        return redirect(reverse('genero') + '?FAIL')