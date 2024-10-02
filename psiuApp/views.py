from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View 
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