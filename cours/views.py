from django.shortcuts import render, redirect, get_object_or_404
from .models import Cours
from .forms import CoursForm

from .models import Enseignant
from .forms import EnseignantForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def acceuil(request):
    return render(request, 'cours/acceuil.html')

@login_required
def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'cours/liste_cours.html', {'cours': cours})

@login_required
def ajouter_cours(request):
    form = CoursForm()
    
    if request.method == 'POST':
        form = CoursForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('liste_cours')
        
    return render(request, 'cours/ajouter_cours.html', {'form': form})

@login_required
def modifier_cours(request, id):
    cours = get_object_or_404(Cours, id=id)

    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cours)

        if form.is_valid():
            form.save()
            return redirect('liste_cours')
    else:
        form = CoursForm(instance=cours)

    return render(request, 'cours/modifier_cours.html', {'form': form})
        
@login_required
def supprimer_cours(request, id):
    cours = get_object_or_404(Cours, id = id)
    cours.delete()
    return redirect('liste_cours')


# Section pour les enseignants
@login_required
def liste_enseignants(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'enseignants/liste_enseignants.html', {'enseignants': enseignants})

@login_required
def ajouter_enseignants(request):
    form = EnseignantForm()
    
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
        
    return render(request, 'enseignants/ajouter_enseignants.html', {'form': form})

@login_required
def modifier_enseignants(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)

    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)

        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    else:
        form = EnseignantForm(instance=enseignant)

    return render(request, 'enseignants/modifier_enseignants.html', {'form': form})

@login_required
def supprimer_enseignants(request, id):
    enseignant = get_object_or_404(Enseignant, id = id)
    enseignant.delete()
    return redirect('liste_enseignants')


# Authentification et autorisation
def connexion_utilisateur(request):  
    message = ""
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            next_url = request.GET.get('next')

            if next_url:
                return redirect(next_url)
            else:
                return redirect('liste_cours')

        else:
            message = "Nom d'utilisateur ou mot de passe incorrect."

    return render(request, 'cours/connexion.html', {'message': message})

@login_required
def deconnexion_utilisateur(request):
    logout(request)
    return redirect('connexion_utilisateur')

