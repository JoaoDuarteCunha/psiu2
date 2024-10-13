from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Atividade(models.Model):
  id = models.AutoField(primary_key=True)

  #Todas as atividades
  criador = models.ForeignKey(User, on_delete=models.CASCADE)
  dataHora = models.DateTimeField(auto_now_add=False, blank=True, null=True)

  localSaida = models.CharField(verbose_name='Local de Saída', max_length=30,null=True, blank=True)
  localChegada = models.CharField(max_length=30,null=True, blank=True)
  vagas = models.IntegerField(default=4,null=True)
  adicionais = models.CharField(max_length=254, blank=True, default='')

  materia = models.CharField(max_length=10,blank=True)
  local = models.CharField(max_length=30,blank=True)
  nome = models.CharField(max_length=30,blank=True)
  atividade = models.CharField(max_length=30,blank=True)
  interesses = models.CharField(max_length=30,blank=True)

  tipo = models.CharField(max_length=15,null=True)

  def __str__(self): 
    return self.nome 
  
class ParticipaAtividade(models.Model):
  participante = models.ForeignKey(User, on_delete=models.CASCADE)
  atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)