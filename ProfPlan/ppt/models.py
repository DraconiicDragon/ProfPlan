from django.db import models
from calendario.models import Calendario
from Disciplinas.models import Disciplina
from django.contrib.auth.models import User

# Create your models here.

class Ppt(models.Model):
    serie_periodo = models.PositiveSmallIntegerField()
    turma = models.CharField(max_length=10)
    trimestre_semestre = models.CharField(max_length=10)
    ementa = models.TextField()
    objetivos = models.TextField()
    cidade = models.CharField(max_length=50)

    aulas_segunda = models.PositiveSmallIntegerField()
    aulas_terca = models.PositiveSmallIntegerField()
    aulas_quarta = models.PositiveSmallIntegerField()
    aulas_quinta = models.PositiveSmallIntegerField()
    aulas_sexta = models.PositiveSmallIntegerField()

    calendario = models.ForeignKey(
        Calendario,
        on_delete=models.CASCADE
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

class TipoAtividade(models.Model):
    nome = models.CharField(max_length=50)

class AtividadeAvaliativa(models.Model):
    conteudo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    tipo = models.ForeignKey(
        TipoAtividade,
        on_delete=models.CASCADE
    )

class Semana(models.Model):
    inicio = models.DateField()
    fim = models.DateField()
    conteudo_programatico = models.CharField(max_length=50)
    metodologia = models.CharField(max_length=50)
    ppt = models.ForeignKey(
        Ppt,
        on_delete=models.CASCADE
    )
    atividade_avaliativa = models.ForeignKey(
        AtividadeAvaliativa,
        on_delete=models.CASCADE
    )
