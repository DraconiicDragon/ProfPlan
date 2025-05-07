from django.shortcuts import render
from .forms import CursoForm

# Create your views here.

def curso_form(request):
    form = CursoForm()
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "disciplinas/curso.html", context)