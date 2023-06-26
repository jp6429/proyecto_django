from django.urls import path
from .views import *

urlpatterns = [
    path('',root),
    path('mascotas/', mascotas_list, name="mascotas-list"),
    path('mascotas/new', mascotas_new, name='mascotas-new'),
    path('mascotas/edit/<str:videogame_id>', mascotas_edit, name="mascotas-edit"),
    path('mascotas/delete/<str:videogame_id>', mascotas_delete, name="mascotas-delete"),
    path('mascotas/detail/<str:videogame_id>', mascotas_detail, name="mascotas-detail"),
    path('mascotas/mascotType/<mascotType>', mascotas_by_mascotType, name="mascotas-mascotType"),
]