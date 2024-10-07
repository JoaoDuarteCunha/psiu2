from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import View 
from psiuApp.forms import AtividadeModel2Form
from psiuApp.models import Atividade
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 

# Create your views here.
def home(request): 
    # processamento antes de mostrar a home page 
    return render(request, 'psiuApp/home.html') 

def segundaPagina(request): 
    # processamento antes de mostrar a segunda página 
    return render(request, 'psiuApp/segunda.html') 


class AtividadeListView(LoginRequiredMixin, View): 
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

@login_required
def logout(request): 
    return render(request, 'psiuApp/logout.html') 