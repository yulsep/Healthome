""" from rest_framework import generics, status
from api.models.auxiliar import Auxiliar
from api.serializers import AuxiliarSerializer

class AuxiliarDetailView(generics.RetrieveAPIView):
    queryset = Auxiliar.objects.all()
    serializer_class = AuxiliarSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs) """