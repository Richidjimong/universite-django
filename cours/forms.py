from django import forms
from .models import Cours
from .models import Enseignant

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['titre', 'description', 'credit', 'enseignant']
        
class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'specialite']