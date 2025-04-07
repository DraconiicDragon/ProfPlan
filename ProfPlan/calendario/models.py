from django.db import models

# Create your models here.

class Calendario(models.Model):
    codigo = models.CharField(max_length=6)
    inicio = models.DateField()
    fim = models.DateField()

class FeriadoFixo(models.Model):
    data = models.DateField()
    nome = models.CharField(max_length=50)
    calendario = models.ManyToManyField(Calendario)

class NomeFeriadoMovel(models.Model):
    nome = models.CharField(max_length=50)

class FeriadoMovel(models.Model):
    data = models.DateTimeField()
    nome = models.ForeignKey(
        NomeFeriadoMovel,
        on_delete = models.CASCADE
    )
    calendario = models.ForeignKey(
        Calendario,
        on_delete = models.CASCADE
    )

class SabadoLetivo(models.Model):
    data = models.DateField()
    dia_referente = models.PositiveSmallIntegerField()

