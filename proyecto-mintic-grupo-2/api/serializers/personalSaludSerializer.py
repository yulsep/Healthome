from dataclasses import fields
from rest_framework import serializers
from api.models.personalSalud import PersonalSalud

class PersonalSaludSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PersonalSalud
        fields = ('idUsuario','especialidad','registro')