""" from rest_framework import status, views
from rest_framework.response import Response
from api.serializers.medicoSerializer import MedicoSerializer

class MedicoCreateView(views.APIView):

    def post(self,request,*args,**kwargs):
        serializer = MedicoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data,status = status.HTTP_201_CREATED) """