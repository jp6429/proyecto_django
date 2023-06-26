from django.shortcuts import render, HttpResponse, redirect
from crud.models import *

# Create your views here.
def root(request):
    return redirect('home')

def home(request):
    return render(request,'core/home.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def contacto(request):
    return render(request,'core/contacto.html')

def mascotas(request):
    context = {'mascotas':Mascot.objects.all()}
    return render(request,'core/mascotas.html',context)

def content1(request):
    return render(request,'core/content1.html')

def content2(request):
    return render(request,'core/content2.html')

def content3(request):
    return render(request,'core/content3.html')

def mascotas_by_mascotType(request,mascotType):
    context = {'mascotas':Mascot.objects.filter(mascotType=mascotType)}
    return render(request,'core/mascotas.html',context)
