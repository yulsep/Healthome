from django.db import models
from .user import User

class Auxiliar(models.Model):
    id=models.AutoField(primary_key=True)
    idUsuario=models.ForeignKey(User, related_name='auxiliar', on_delete=models.CASCADE)