from .models import Curso, Disciplina, DisciplinaProfessor
from django import forms

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

class DisciplinaProfessorForm(forms.ModelForm):
    class Meta:
        model = DisciplinaProfessor
        fields = '__all__'