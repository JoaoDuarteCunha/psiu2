from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Atividade(models.Model):
  id = models.AutoField(primary_key=True)

  #Todas as atividades
  criador = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  vagas = models.PositiveIntegerField(default=4)
  adicionais = models.CharField(verbose_name='Observações', max_length=254, blank=True, default='')
  data = models.DateField(auto_now_add=False)
  hora = models.TimeField(auto_now_add=False)

class Carona(Atividade):
  localSaida = models.CharField(verbose_name='Saindo de', max_length=30)
  localChegada = models.CharField(verbose_name='Destino', max_length=30)

class Extracurriculares(Atividade):
  atividade = models.CharField(max_length=30)
  local = models.CharField(max_length=30)

class Estudos(Atividade):
  materia = models.CharField(verbose_name='Disciplina', max_length=10)
  local = models.CharField(max_length=30)

class Liga(Atividade):
  nome = models.CharField(verbose_name='Nome da Liga', max_length=30)
  local = models.CharField(max_length=30)

class ConhecerPessoas(Atividade):
  atividade = models.CharField(max_length=30)
  local = models.CharField(max_length=30)

class ParticipaAtividade(models.Model):
  participante = models.ForeignKey(User, on_delete=models.CASCADE)
  atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)