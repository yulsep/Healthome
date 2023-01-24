from django.db import models
from .user import User

class PersonalSalud(models.Model):
    id=models.AutoField(primary_key=True)
    idUsuario=models.ForeignKey(User, related_name='personalSalud', on_delete=models.CASCADE)
    especialidad=models.CharField('Especialidad', max_length=60)
    registro=models.CharField('Registro', max_length=60)