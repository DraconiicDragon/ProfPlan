from django.shortcuts import render
from .forms import *

# Create your views here.

def curso_form(request):
    title = "Cadastrar Curso"
    form = CursoForm()
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form, "title": title}
    return render(request, "forms.html", context)

def disciplina_form(request):
    title = "Cadastrar Disciplina"
    form = DisciplinaForm()
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form, "title": title}
    return render(request, "forms.html", context)