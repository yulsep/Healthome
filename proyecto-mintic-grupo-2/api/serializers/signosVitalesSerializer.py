from dataclasses import fields
from rest_framework import serializers
from api.models.signosVitales import SignosVitales

class SignosVitalesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SignosVitales
        fields = ('oximetria','frecuenciaRespiratoria','frecuenciaCardiaca','temperatura','presionArterial','glicemias','idPaciente')