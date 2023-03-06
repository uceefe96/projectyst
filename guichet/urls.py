from django.urls import path, include 
from . import views


urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('selectionner-etudiant/', views.selectionner_etudiant, name='selectionner_etudiant'),
    path('bilan-de-notes/<int:etudiant_id>/', views.bilan_de_notes, name='bilan_de_notes'),
    path('attestation-universitaire/<int:etudiant_id>/', views.attestation_universitaire, name='attestation_universitaire'),
    path('attestation-d-inscription/<int:etudiant_id>/', views.attestation_d_inscription, name='attestation_d_inscription'),
    path('login', views.login, name='LoginForm' )
]
