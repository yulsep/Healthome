'''from dataclasses import fields
from rest_framework import serializers
from api.models.personalSalud import PersonalSalud

class MedicoSerializer(serializers.ModelSerializer):
    #medico = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = PersonalSalud
        fields =  '__all__' #('id','especialidad','registro')'''