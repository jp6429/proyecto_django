from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def root(request):
    return redirect('home')

def home(request):
    return render(request,'core/home.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def contacto(request):
    return render(request,'core/contacto.html')

def galeria(request):
    return render(request,'core/galeria.html')

def content1(request):
    return render(request,'core/content1.html')

def content2(request):
    return render(request,'core/content2.html')

def content3(request):
    return render(request,'core/content3.html')
