from rest_framework import generics, status
from api.models.paciente import Paciente
from api.serializers import PacienteSerializer

class PacienteDetailView(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)