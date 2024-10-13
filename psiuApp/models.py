from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Atividade(models.Model):
  id = models.AutoField(primary_key=True)

  #Todas as atividades
  criador = models.ForeignKey(User, on_delete=models.CASCADE)
  dataHora = models.DateTimeField(auto_now_add=False, blank=True, null=True)
  vagas = models.IntegerField(default=4,null=True)
  local = models.CharField(max_length=30,blank=True)

class Carona(Atividade):
  localSaida = models.CharField(verbose_name='Local de Saída', max_length=30,null=True, blank=True)
  localChegada = models.CharField(max_length=30,null=True, blank=True)

  def get_classe(Carona):
    return 'Carona'


class Extracurriculares(Atividade):
  atividade = models.CharField(max_length=30,blank=True)
  adicionais = models.CharField(max_length=254, blank=True, default='')


class Estudos(Atividade):
  materia = models.CharField(max_length=10,blank=True)

class Liga(Atividade):
  nome = models.CharField(max_length=30,blank=True)


class ConhecerPessoas(Atividade):
  atividade = models.CharField(max_length=30,blank=True)


class ParticipaAtividade(models.Model):
  participante = models.ForeignKey(User, on_delete=models.CASCADE)
  atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)