from django.contrib import admin
from .models import Calendario, SabadoLetivo, FeriadoFixo, FeriadoMovel

# Register your models here.

admin.site.register(Calendario)
admin.site.register(SabadoLetivo)
admin.site.register(FeriadoMovel)
admin.site.register(FeriadoFixo)