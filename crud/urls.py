from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('mascots/', mascots_list, name="mascots"),
    path('mascots/<str:mascotas_id>/delete', mascots_delete, name="mascots-delete"),
    path('mascots/detail/<str:mascotas_id>', mascots_detail, name="mascotas-detail"),
    path('mascots/edit/<str:mascotas_id>', mascots_update, name="mascotas-edit"),
    path('mascots/new/', mascots_new, name="mascotas-new"),
    path('mascots/mascotType/<mascotType>', mascots_by_mascotType, name="mascotas-mascotType"),
    path('mascots/gender/<gender>', mascots_by_gender, name="mascotas-gender"),
    path('contact/', contact, name='contact'),
    path('mascotsType/', mascotsType_list, name="mascotasType"),
    path('mascotsType/<str:mascotasTipo_id>/delete', mascotsType_delete, name="mascotasType-delete"),
    path('mascotsType/detail/<str:mascotasTipo_id>', mascotsType_detail, name="mascotasType-detail"),
    path('mascotsType/edit/<str:mascotasTipo_id>', mascotsType_update, name="mascotasType-edit"),
    path('mascotsType/new/', mascotsType_new, name="mascotasType-new"),
    path('gender/', gender_list, name="genero"),
    path('gender/<str:genero_id>/delete', gender_delete, name="genero-delete"),
    path('gender/detail/<str:genero_id>', gender_detail, name="genero-detail"),
    path('gender/edit/<str:genero_id>', gender_update, name="genero-edit"),
    path('gender/new/', gender_new, name="genero-new"),
]