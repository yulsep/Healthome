from django.db import models
from .historiaClinica import HistoriaClinica

class Sugerencias(models.Model):
    id = models.AutoField(primary_key=True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    idPaciente= models.ForeignKey(HistoriaClinica, related_name="sugerencias", on_delete=models.CASCADE)