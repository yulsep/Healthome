from rest_framework import generics, status
from api.models.signosVitales import SignosVitales
from api.serializers import SignosVitalesSerializer

class SignosVitalesDetailView(generics.RetrieveAPIView):
    queryset = SignosVitales.objects.all()
    serializer_class = SignosVitalesSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)