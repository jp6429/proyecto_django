from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('home/', home, name='home'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
]