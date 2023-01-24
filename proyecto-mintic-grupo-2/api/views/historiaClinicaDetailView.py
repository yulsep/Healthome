from rest_framework import generics, status
from api.models.historiaClinica import HistoriaClinica
from api.serializers import HistoriaClinicaSerializer

class HistoriaClinicaDetailView(generics.RetrieveAPIView):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)