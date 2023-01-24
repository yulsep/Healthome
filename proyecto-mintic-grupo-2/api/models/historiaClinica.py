from django.db import models
from .signosVitales import SignosVitales

class HistoriaClinica(models.Model):
    id = models.AutoField(primary_key=True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    diagnostico = models.CharField("Diagnostico", max_length=150)
    descripcion = models.TextField()
    entorno = models.TextField()
    idSignosVitales = models.ForeignKey(SignosVitales, related_name="historiaClinica", on_delete=models.CASCADE)