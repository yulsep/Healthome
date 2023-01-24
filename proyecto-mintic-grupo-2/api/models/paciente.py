from django.db import models
from .user import User
from .personalSalud import PersonalSalud

class Paciente(models.Model):
    id=models.AutoField(primary_key=True)
    idUsuario=models.ForeignKey(User, related_name='paciente', on_delete=models.CASCADE)
    fechaNacimiento=models.DateField('FechaNacimiento')
    ciudad=models.CharField('Ciudad', max_length=50)
    direccion=models.CharField('Direccion', max_length=150)
    idPersonalSalud = models.ForeignKey(PersonalSalud, related_name='paciente', on_delete=models.CASCADE)