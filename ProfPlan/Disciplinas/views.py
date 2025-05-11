from django.shortcuts import render
from .forms import CursoForm, DisciplinaForm, DisciplinaProfessorForm
from .models import Curso, Disciplina

# Create your views here.

formsPage = "forms.html"
listPage = "list.html"

def curso_form(request):
    title = "Cadastrar Curso"
    form = CursoForm()
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form, "title": title}
    return render(request, formsPage, context)

def view_cursos(request):
    title = "Cursos"
    offset = 0
    limit = 10
    list = Curso.objects.all().values('nome', 'codigo', 'modalidade_ensino__descricao')[offset : limit]    
    context = {
        "list" : list,
        "title" : title,
        "headers" : ('Nome', 'Código', 'Modalidade')
    }
    return render(request, listPage, context)

def disciplina_form(request):
    title = "Cadastrar Disciplina"
    form = DisciplinaForm()
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form, "title": title}
    return render(request, formsPage, context)

def view_disciplinas(request):
    title = "Disciplinas"
    offset = 0
    limit = 10
    list = Disciplina.objects.all().values('nome', 'curso__nome')[offset : limit]
    context = {
        "list" : list,
        "title" : title,
        "headers" : ('Nome', 'Curso')
    }
    return render(request, listPage, context)
    


def disciplina_professor_form(request):
    title = "Cadastrar Disciplina"
    form = DisciplinaProfessorForm()
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form, "title": title}
    return render(request, formsPage, context)