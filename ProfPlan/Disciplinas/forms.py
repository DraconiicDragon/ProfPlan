from .models import Curso, Disciplina, DisciplinaMinistrada
from django import forms

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class DisciplinaMinistradaForm(forms.ModelForm):
    class Meta:
        model = DisciplinaMinistrada
        fields = '__all__'