from django.db import models
from .paciente import Paciente

class SignosVitales(models.Model):
    id = models.AutoField(primary_key=True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    oximetria = models.FloatField()
    frecuenciaRespiratoria = models.FloatField()
    frecuenciaCardiaca = models.FloatField()
    temperatura = models.FloatField()
    presionArterial = models.CharField('PresionArterial', max_length=10)
    glicemias = models.FloatField()
    idPaciente= models.ForeignKey(Paciente, related_name="signosVitales", on_delete=models.CASCADE)