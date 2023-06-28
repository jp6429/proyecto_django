from rest_framework import serializers
from crud.models import *

class MascotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascot
        fields = (
            'idMascot','name','mascotType','breed','gender','created_at','updated_at'
        )

class MascotTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MascotType
        fields = (
            'id','mascotType'
        )