from rest_framework import generics, status
from api.models.familiar import Familiar
from api.serializers import FamiliarSerializer

class FamiliarDetailView(generics.RetrieveAPIView):
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)