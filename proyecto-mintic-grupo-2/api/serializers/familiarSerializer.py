from dataclasses import fields
from rest_framework import serializers
from api.models.familiar import Familiar

class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familiar
        fields = ('idUsuario','parentezco','eMail','idPaciente')