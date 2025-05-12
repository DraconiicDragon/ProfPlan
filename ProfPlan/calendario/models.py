from django.db import models

# Create your models here.

class Calendario(models.Model):
    codigo = models.CharField(max_length=6)
    inicio = models.DateField()
    fim = models.DateField()

    def __str__(self):
        return self.codigo

class FeriadoFixo(models.Model):
    data = models.DateField()
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.data + ' - ' + self.nome

class FeriadoFixoCalendario(models.Model):
    feriado = models.ForeignKey(
        FeriadoFixo,
        on_delete = models.CASCADE
    )
    calendario = models.ForeignKey(
        Calendario,
        on_delete= models.CASCADE
    )

    def __str__(self):
        return self.calendario.codigo + ' - ' + self.feriado.nome

class NomeFeriadoMovel(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

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

    def __str__(self):
        return self.data + ' - ' + self.nome.nome

class SabadoLetivo(models.Model):
    data = models.DateField()
    dia_referente = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.data + ' - ' + self.dia_referente

