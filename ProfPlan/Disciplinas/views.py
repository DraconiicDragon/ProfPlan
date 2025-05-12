from django.shortcuts import render
from .forms import CursoForm, DisciplinaForm, DisciplinaMinistradaForm
from .models import Curso, Disciplina, DisciplinaMinistrada

# Create your views here.

formsPage = "forms.html"
listPage = "list.html"

def curso_form(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return view_cursos(request)
        
    if request.method == 'GET':
        title = "Cadastrar Curso"
        form = CursoForm()
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
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return view_disciplinas(request)
        
    if request.method == 'GET':
        title = "Cadastrar Disciplina"
        form = DisciplinaForm()
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
    
def disciplina_ministrada_form(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return view_disciplinas_ministradas(request)
        
    if request.method == 'GET':
        title = "Cadastrar Ministrante"
        form = DisciplinaMinistradaForm()
        context = {"form" : form, "title": title}
        return render(request, formsPage, context)

def view_disciplinas_ministradas(request):
    title = 'Disciplinas Ministradas'
    offset = 0
    limit = 10
    list = DisciplinaMinistrada.objects.all().values('ano', 'disciplinas__nome', 'usuario__first_name', 'turma')[offset : limit]
    context = {
        "list" : list,
        "title" : title,
        "headers" : ('Ano', 'Nome', 'Ministrante', 'Turma')
    }
    return render(request, listPage, context)
