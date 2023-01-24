from rest_framework import generics, status
from api.models.personalSalud import PersonalSalud
from api.serializers import PersonalSaludSerializer

class PersonalSaludDetailView(generics.RetrieveAPIView):
    queryset = PersonalSalud.objects.all()
    serializer_class = PersonalSaludSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)