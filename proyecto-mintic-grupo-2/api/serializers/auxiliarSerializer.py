from dataclasses import fields
from rest_framework import serializers
from api.models.auxiliar import Auxiliar

class AuxiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auxiliar
        fields = ('id')