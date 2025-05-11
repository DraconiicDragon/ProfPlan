from django.urls import path
from .views import curso_form, disciplina_form, disciplina_professor_form
from .views import view_cursos, view_disciplinas

urlpatterns = [
    path('curso/new', curso_form),
    path('cursos', view_cursos),
    path('disciplina/new', disciplina_form),
    path('disciplinas', view_disciplinas),
    path('disciplinaprofessor/new', disciplina_professor_form)
]