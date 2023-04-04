from django.http import JsonResponse
from .serializer import VoituresSerializer
from . import models
from django.views.decorators.csrf import csrf_exempt

def index(request):
    voitures = models.Voitures.objects.all()
    serializer = VoituresSerializer(voitures, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def testPost(request):

    name = request.POST.get("name")
    couleur = request.POST.get("couleur")
    prix = request.POST.get("prix")

    print(list(request.POST.keys()))
    print(couleur)
    # voiture = models.Voitures(name, couleur, prix)
    # voiture.save()
    return JsonResponse({'salut': 'ca va '})