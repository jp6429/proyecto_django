from django.shortcuts import render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.http.response import JsonResponse

from crud.models import *
from .serializers import *

# Create your views here.

@api_view(['GET','POST','DELETE'])
def mascot_list(request):
    if request.method == 'GET':
        mascotas = Mascot.objects.all()

        name = request.query_params.get('name',None)
        if name is not None:
            mascotas = mascotas.filter(name__contains=name)

        breed = request.query_params.get('breed',None)
        if breed is not None:
            mascotas = mascotas.filter(breed__contains=breed)

        mascotType = request.query_params.get('mascotType',None)
        if mascotType is not None:
            mascotas = mascotas.filter(mascotType__mascotType__contains=mascotType)

        mascotas_serializer = MascotSerializer(mascotas,many=True)
        return Response(mascotas_serializer.data)
    
    elif request.method == 'POST':
        mascotas_data = JSONParser().parse(request)
        mascotas_serializer = MascotSerializer(data=mascotas_data)
        if mascotas_serializer.is_valid():
            mascotas_serializer.save()
            return JsonResponse(mascotas_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(mascotas_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cantidad = Mascot.objects.all().delete()
        return Response({'mensaje':'Se han eliminado {} mascotas de la base de datos.'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def mascot_detail(request, mascot_id):
    try:
        mascotas = Mascot.objects.get(idMascot=mascot_id)
    except:
        return Response({'mensaje':'La mascota {} no existe en nuestros registros.'.format(mascot_id)},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        mascotas_serializer = MascotSerializer(mascotas)
        return Response(mascotas_serializer.data)
    
    elif request.method == 'PUT':
        mascotas_data = JSONParser().parse(request)
        mascotas_serializer = MascotSerializer(mascotas,data=mascotas_data)
        if mascotas_serializer.is_valid():
            mascotas_serializer.save()
            return JsonResponse(mascotas_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(mascotas_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        mascotas.delete()
        return Response({'mensaje':'La mascota {} ha sido eliminada de la base de datos'.format(mascot_id)},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def mascotType_list(request):
    if request.method == 'GET':
        mascotType = MascotType.objects.all()
        mascotType_serializer = MascotTypeSerializer(mascotType,many=True)
        return Response(mascotType_serializer.data)

    elif request.method == 'POST':
        mascotType_data = JSONParser().parse(request)
        mascotType_serializer = MascotTypeSerializer(data=mascotType_data)
        if mascotType_serializer.is_valid():
            mascotType_serializer.save()
            return JsonResponse(mascotType_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(mascotType_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
