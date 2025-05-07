from django.urls import path
from .views import curso_form

urlpatterns = [
    path('create/', curso_form),
]