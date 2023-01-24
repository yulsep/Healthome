from dataclasses import fields
from rest_framework import serializers
from api.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('rol','nombre','apellido','celular','genero','username','password')