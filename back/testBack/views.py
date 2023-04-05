from django.http import JsonResponse
from .serializer import VoituresSerializer
from . import models
from django.views.decorators.csrf import csrf_exempt


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class VoitureAPIView(APIView):
    def post(self, request):
        name = request.data.get("name")
        couleur = request.data.get("couleur")
        prix = request.data.get("prix")

        voiture = models.Voitures(name=name, couleur=couleur, prix=prix )
        voiture.save()

        return JsonResponse({'data': [name, couleur, prix]}, status=status.HTTP_200_OK)

    def get(self,request):
        voitures = models.Voitures.objects.all()
        serializer = VoituresSerializer(voitures, many=True)

        return JsonResponse(serializer.data, safe=False)

    def delete(self, request):
        id = request.data.get("id")
        voiture = models.Voitures.objects.get(id_voiture=id)
        voiture.delete()

        return JsonResponse({'message': 'Voiture deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    def put(self, request):
        voiture = models.Voitures.objects.get(id_voiture= request.data.get("id_voiture"))

        voiture.name = request.data.get("name", request.data.get("name"))
        voiture.couleur = request.data.get("couleur", request.data.get("couleur"))
        voiture.prix = request.data.get("prix", request.data.get("prix"))
        voiture.save()

        return JsonResponse({'data': [voiture.name, voiture.couleur, voiture.prix]}, status=status.HTTP_200_OK)


class MessageAPIView(APIView):
    def post(self, request):
        message = request.data.get('message')
        return Response({'message': message}, status=status.HTTP_200_OK)