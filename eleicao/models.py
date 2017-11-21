from django.db import models

# Create your models here.
class Candidato(models.Model):
    nome = models.CharField(max_length=128)
    votos = models.IntegerField(null=True, blank=True, max_length=None)
    def __str__(self):
        return "{}".format(self.nome)
class Voto (models.Model):
    candidato = models.ForeignKey(Candidato,null=True, blank=True)
    def __str__(self):
            return "{}".format(self.candidato)
class VotoBranco (models.Model):
    CHOICES = (('True', 'Branco'),)
    branco = models.CharField(max_length=20, choices=CHOICES)
    def __str__(self):
        return "{}".format("Branco")
class Eleicao(models.Model):
    nome = models.CharField(max_length=128)
    data = models.DateField(verbose_name="Data")
    vencedor = models.CharField(max_length=128, null=True, blank=True)
    candidatos = models.ManyToManyField(Candidato, related_name="CandidatosEleicao")
    def __str__(self):
        return "{}".format(self.nome)

class Eleitor(models.Model):
    nome = models.CharField(max_length=128)
    token = models.CharField(max_length=128, null=True, blank=True)
    votou = models.NullBooleanField(verbose_name="VOTOU: ")
    def __str__(self):
        return "{} - {}".format(self.nome, self.votou)