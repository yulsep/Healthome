from rest_framework import generics, status
from api.models.sugerencias import Sugerencias
from api.serializers import SugerenciasSerializer

class SugerenciasDetailView(generics.RetrieveAPIView):
    queryset = Sugerencias.objects.all()
    serializer_class = SugerenciasSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)