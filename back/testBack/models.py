from django.db import models

# Create your models here.

class Voitures(models.Model):
    id_voiture = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    couleur = models.CharField(max_length=50, blank=True, null=True)
    prix = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voitures'
