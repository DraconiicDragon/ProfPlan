from django.urls import path
from .views import *

urlpatterns = [
    path('curso/new', curso_form),
    path('disciplina/new', disciplina_form)
]