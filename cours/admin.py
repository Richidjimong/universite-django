from django.contrib import admin
from .models import Cours, Enseignant

# Register your models here.
admin.site.register(Enseignant)
admin.site.register(Cours)
