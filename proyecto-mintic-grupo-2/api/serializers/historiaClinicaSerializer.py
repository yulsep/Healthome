from dataclasses import fields
from rest_framework import serializers
from api.models.historiaClinica import HistoriaClinica

class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = ('diagnostico','descripcion','entorno','idSignosVitales')