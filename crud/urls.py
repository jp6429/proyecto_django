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
]