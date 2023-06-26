from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('home/', home, name='home'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('mascotas/', mascotas, name='mascotas'),
    path('content1/', content1, name='content1'),
    path('content2/', content2, name='content2'),
    path('content3/', content3, name='content3'),
    path('mascotas/mascotType/<mascotType>', mascotas_by_mascotType, name="mascotas-mascotType"),
]