from django.db import models

# Create your models here.
from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    cin = models.CharField(max_length=255)
    cne = models.CharField(max_length=255)
    num_tel = models.CharField(max_length=255)
    email = models.EmailField()
    date_de_naissance = models.DateField()
    date_d_inscription = models.DateField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Module(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='modules')
    nom = models.CharField(max_length=255)
    note = models.FloatField()

    def __str__(self):
        return f"{self.nom} ({self.note})"

