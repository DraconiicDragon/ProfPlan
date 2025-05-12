from django.contrib import admin
from .models import ModalidadeEnsino, Curso, DisciplinaMinistrada, Disciplina
# Register your models here.

admin.site.register(ModalidadeEnsino)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(DisciplinaMinistrada)