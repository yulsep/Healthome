from django.db import models
from .paciente import Paciente
from .user import User

class Familiar(models.Model):
    id=models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(User, related_name='familiar', on_delete=models.CASCADE)
    parentezco=models.CharField('Parentezco', max_length=50)
    eMail=models.EmailField('Correo', max_length=50)
    idPaciente=models.ForeignKey(Paciente, related_name='familiar', on_delete=models.CASCADE)