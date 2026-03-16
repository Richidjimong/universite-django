from django.urls import path
from .views import acceuil, ajouter_cours, liste_cours, modifier_cours, supprimer_cours
from .views import ajouter_enseignants, liste_enseignants, modifier_enseignants, supprimer_enseignants
from .views import connexion_utilisateur, deconnexion_utilisateur

urlpatterns = [
    path('', acceuil, name='acceuil'),
    path('cours/', liste_cours, name='liste_cours'),
    path('ajouter/', ajouter_cours, name='ajouter_cours'),
    path('modifier/<int:id>/', modifier_cours, name='modifier_cours'),
    path('supprimer/<int:id>/', supprimer_cours, name='supprimer_cours'),
    
    # Section pour les enseignants
    path('enseignants/', liste_enseignants, name='liste_enseignants'),
    path('enseignants/ajouter/', ajouter_enseignants, name='ajouter_enseignants'),
    path('enseignants/modifier/<int:id>/', modifier_enseignants, name='modifier_enseignants'),
    path('enseignants/supprimer/<int:id>/', supprimer_enseignants, name='supprimer_enseignants'),
    
    # Authentification et autorisation
    path('connexion/', connexion_utilisateur, name='connexion_utilisateur'),
    path('deconnexion/', deconnexion_utilisateur, name='deconnexion_utilisateur'),
]