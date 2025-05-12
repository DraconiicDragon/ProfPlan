from django.shortcuts import render
from .forms import CalendarioForm
from .models import Calendario

# Create your views here.

formsPage = 'forms.html'
listPage = 'list.html'

def calendario_form(request):
    if request.method == 'POST':
        form = CalendarioForm(request.POST)
        if form.is_valid():
            form.save()
            return view_calendarios(request)
    
    if request.method == 'GET':
        title = 'Cadastrar Calendário'
        form = CalendarioForm()
        context = {'form': form, 'title': title}
        return render(request, formsPage, context)
    
def view_calendarios(request):
    title = 'Calendários'
    offset = 0
    limit = 10
    list = Calendario.objects.all().values('codigo', 'inicio', 'fim')[offset : limit]
    context = {
        'title' : title,
        'list' : list,
        'headers' : ('Código', 'Ínicio', 'Fim')
    }
    return render(request, listPage, context)