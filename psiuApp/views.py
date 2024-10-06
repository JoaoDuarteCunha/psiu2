from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
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