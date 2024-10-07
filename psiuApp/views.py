from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.base import View 
from psiuApp.forms import AtividadeModel2Form
from psiuApp.models import Atividade

# Create your views here.
def home(request): 
    # processamento antes de mostrar a home page 
    return render(request, 'psiuApp/home.html') 

def segundaPagina(request): 
    # processamento antes de mostrar a segunda página 
    return render(request, 'psiuApp/segunda.html') 

class AtividadeListView(View): 
    def get(self, request, *args, **kwargs): 
        atividades = Atividade.objects.all() 
        contexto = { 'atividades': atividades, } 
        return render( 
            request,  
            'psiuApp/listaAtividades.html',  
            contexto) 

class AtividadeCreateView(View): 
    def get(self, request, *args, **kwargs): 
        contexto = { 'formulario': AtividadeModel2Form, } 
        return render(request, "psiuApp/criaAtividade.html", contexto) 
    def post(self, request, *args, **kwargs): 
        formulario = AtividadeModel2Form(request.POST) 
        if formulario.is_valid(): 
            contato = formulario.save() 
            contato.save() 
            return HttpResponseRedirect(reverse_lazy("psiuApp:lista-atividades")) 

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