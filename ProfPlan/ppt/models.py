from django.db import models
from calendario.models import Calendario
from Disciplinas.models import DisciplinaProfessor

# Create your models here.
class Status(models.Model):
    descricao = models.CharField(max_length=50)

class PedidoPpt(models.Model):
    disciplinaProfessor = models.ForeignKey(
        DisciplinaProfessor,
        on_delete = models.CASCADE
    )
    data_entrega = models.DateField()
    status = models.ForeignKey(
        Status,
        on_delete = models.CASCADE
    )

class Ppt(models.Model):
    serie_periodo = models.PositiveSmallIntegerField()
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
    
    pedido = models.ForeignKey(
        PedidoPpt,
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
