from django.contrib import admin
from .models import Calendario, SabadoLetivo, FeriadoFixo, FeriadoMovel, NomeFeriadoMovel, FeriadoFixoCalendario

# Register your models here.

admin.site.register(Calendario)
admin.site.register(SabadoLetivo)
admin.site.register(FeriadoMovel)
admin.site.register(NomeFeriadoMovel)
admin.site.register(FeriadoFixo)
admin.site.register(FeriadoFixoCalendario)