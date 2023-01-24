from dataclasses import fields
from rest_framework import serializers
from api.models.sugerencias import Sugerencias

class SugerenciasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sugerencias
        fields = ('descripcion','idPaciente')