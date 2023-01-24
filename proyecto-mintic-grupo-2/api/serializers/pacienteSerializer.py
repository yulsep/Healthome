from dataclasses import fields
from rest_framework import serializers
from api.models.paciente import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('idUsuario','fechaNacimiento','ciudad','direccion','idPersonalSalud')