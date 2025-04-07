from django.contrib import admin
from .models import Ppt, AtividadeAvaliativa, Semana, TipoAtividade

# Register your models here.
admin.site.register(Ppt)
admin.site.register(AtividadeAvaliativa)
admin.site.register(Semana)
admin.site.register(TipoAtividade)