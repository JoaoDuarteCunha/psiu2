from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import View 
from psiuApp.forms import AtividadeModel2Form
from psiuApp.models import Atividade
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.views.generic.edit import UpdateView 

listaAtividades = ['carona', 'estudos', 'ligas', 'extracurriculares', 'conhecer_pessoas']
nomeAtividade = {'carona': 'Carona', 
                 'estudos': 'Grupo de Estudos', 
                 'ligas': 'Ligas Acadêmicas', 
                 'extracurriculares': 'Atividades Extracurriculares', 
                 'conhecer_pessoas': 'Conhecer Pessoas'}

# Create your views here.
def home(request): 
    # processamento antes de mostrar a home page 
    return render(request, 'psiuApp/home.html') 

def segundaPagina(request): 
    # processamento antes de mostrar a segunda página 
    return render(request, 'psiuApp/segunda.html') 


class AtividadeListView(View): 
    def get(self, request, tipo, *args, **kwargs): 
        
        if tipo not in listaAtividades:
            return redirect('psiuApp:homepage') 

        atividades = Atividade.objects.filter(tipo=tipo)
        imagem_atividade = 'psiuApp/img/' + tipo + '.png'
        contexto = { 'atividades': atividades, 'tipoAtividade': tipo, 'nomeAtividade': nomeAtividade.get(tipo, 'Não existente'), 'imagem_atividade': imagem_atividade} 

        return render( 
            request,  
            'psiuApp/listaAtividades.html',  
            contexto) 

class AtividadeCreateView(LoginRequiredMixin, View): 
    def get(self, request, tipo, *args, **kwargs): 

        if tipo not in listaAtividades:
            return redirect('psiuApp:homepage') 
        
        contexto = { 'formulario': AtividadeModel2Form, } 
        return render(request, "psiuApp/criaAtividade.html", contexto) 
    
    def post(self, request, tipo, *args, **kwargs):
        formulario = AtividadeModel2Form(request.POST) 
        if formulario.is_valid():
            atividade = formulario.save()
            atividade.tipo = tipo
            atividade.save() 
            return HttpResponseRedirect(reverse_lazy("psiuApp:lista-atividades", args=[tipo,])) 
        
        return HttpResponseRedirect(reverse_lazy("psiuApp:lista-atividades", args=[tipo,])) 

class AtividadeUpdateView(View): 
    def get(self, request, pk, *args, **kwargs): 
        atividade = Atividade.objects.get(pk=pk) 
        formulario = AtividadeModel2Form(instance=atividade) 
        context = {'atividade': formulario, } 
        return render(request, 'psiuApp/atualizaAtividade.html', context) 
     
    def post(self, request, pk, *args, **kwargs): 
        atividade = get_object_or_404(Atividade, pk=pk) 
        formulario = AtividadeModel2Form(request.POST, instance=atividade) 
        if formulario.is_valid(): 
            atividade = formulario.save() # cria uma pessoa com os dados do formulário 
            atividade.save()        # salva uma pessoa no banco de dados 
            return HttpResponseRedirect(reverse_lazy("psiuApp:lista-atividades")) 
        else: 
            contexto = {'atividade': formulario, } 
            return render(request, 'psiuApp/atualizaAtividade.html', contexto) 
        
class AtividadeDeleteView(View): 
    def get(self, request, pk, *args, **kwargs): 
        atividade = Atividade.objects.get(pk=pk) 
        contexto = { 'atividade': atividade, } 
        return render(request, 'psiuApp/apagaAtividade.html', contexto) 
    
    def post(self, request, pk, *args, **kwargs): 
        atividade = Atividade.objects.get(pk=pk) 
        atividade.delete() 
        return HttpResponseRedirect(reverse_lazy("psiuApp:lista-atividades"))

def registro(request): 
    if request.method == 'POST': 
        formulario = UserCreationForm(request.POST) 
        if formulario.is_valid(): 
            formulario.save()
            return redirect('psiuApp:homepage') 
    else: 
        formulario = UserCreationForm() 
        context = {'form': formulario, } 
        return render(request, 'psiuApp/registro.html', context)

 
class PsiuAppUpdateView(UpdateView): 
  def get(self, request, pk, *args, **kwargs): 
    if request.user.id == pk: 
      return super().get(request, pk, args, kwargs) 
    else: 
      return redirect('psiuApp:homepage') 

@login_required
def logout(request): 
    return render(request, 'psiuApp/logout.html') 