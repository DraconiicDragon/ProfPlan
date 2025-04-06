from django.contrib import admin
from .models import Modalidade_Ensino, Curso, Disciplina

# Register your models here.

admin.site.register(Modalidade_Ensino)
admin.site.register(Curso)
admin.site.register(Disciplina)