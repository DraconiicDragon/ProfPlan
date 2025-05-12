from django.urls import path
from .views import curso_form, disciplina_form, disciplina_ministrada_form
from .views import view_cursos, view_disciplinas, view_disciplinas_ministradas

urlpatterns = [
    path('curso/new', curso_form),
    path('cursos', view_cursos),
    path('disciplina/new', disciplina_form),
    path('disciplinas', view_disciplinas),
    path('disciplinaministrada/new', disciplina_ministrada_form),
    path('disciplinasministradas', view_disciplinas_ministradas),
]