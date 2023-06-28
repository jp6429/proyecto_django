from django.urls import path
from .views import *

urlpatterns = [
    path('mascotas/', mascot_list),
    path('mascotas/<str:mascot_id>', mascot_detail),
    path('mascotType/', mascotType_list),
]