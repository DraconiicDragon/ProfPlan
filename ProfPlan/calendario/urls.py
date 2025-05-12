from django.urls import path
from .views import calendario_form
from .views import view_calendarios

urlpatterns = [
    path('calendarios', view_calendarios),
    path('calendario/new', calendario_form),
]
