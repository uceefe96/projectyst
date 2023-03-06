# serializers.py
#c'est le dossier qui relié les models avec views

from rest_framework import serializers
from .models import Etudiant, Module


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['nom', 'note', 'ects']


class EtudiantSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Etudiant
        fields = ['id', 'nom', 'prenom', 'cin', 'cne', 'num_tel', 'email', 'date_naissance', 'date_inscription', 'modules']


#uuid et slug pour recuperer les informations de la data bases 
# on peux faire 'pk'
# les precedantes'uuid' et 'slug' pour les data bases plus grande  