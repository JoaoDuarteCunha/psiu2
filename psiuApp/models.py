from django.db import models

# Create your models here.
class Atividade(models.Model):
  id = models.AutoField(primary_key=True)
  #criador = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
  #sala = models.OneToOneField(Room, on_delete=models.CASCADE,null=True,blank=True)
  localSaida = models.CharField(max_length=30,null=True, blank=True)
  localChegada = models.CharField(max_length=30,null=True, blank=True)
  dataHora = models.DateTimeField(auto_now_add=False, blank=True, null=True)#Just to prove it
  vagas = models.IntegerField(default=4,null=True)
  adicionais = models.CharField(max_length=254, blank=True, default='')
  dataModificacao = models.DateTimeField(auto_now_add=True, blank=False)
  materia = models.CharField(max_length=10,blank=True)
  local = models.CharField(max_length=30,blank=True)
  nome = models.CharField(max_length=30,blank=True)
  atividade = models.CharField(max_length=30,blank=True)
  interesses = models.CharField(max_length=30,blank=True)

  def __str__(self): 
    return self.nome 