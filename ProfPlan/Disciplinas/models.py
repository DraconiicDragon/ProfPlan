from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Modalidade_Ensino(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    modalidade_ensino = models.ForeignKey(
        Modalidade_Ensino,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria_presencial = models.PositiveSmallIntegerField()
    carga_horaria_remota = models.PositiveSmallIntegerField()
    referencias_basicas = models.TextField()
    referencias_complementares = models.TextField()
    curso = models.ForeignKey(
        Curso,
        on_delete = models.CASCADE
    )
    
    def __str__(self):
        return self.curso.codigo + "." + self.nome
    
class DisciplinaProfessor(models.Model):
    serie_periodo = models.PositiveSmallIntegerField()
    turma = models.CharField(max_length=10)

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    disciplinas = models.ForeignKey(
        Disciplina,
        on_delete=models.CASCADE
    )


