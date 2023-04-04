from rest_framework import serializers
from .models import Voitures

class VoituresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voitures
        fields = ('id_voiture', 'name', 'couleur', 'prix')