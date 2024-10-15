from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import View 
from psiuApp.forms import CaronaModel2Form, EstudosModel2Form, ExtracurricularesModel2Form, ConhecerPessoasModel2Form, LigasModel2Form
from psiuApp.models import Atividade
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.views.generic.edit import UpdateView 
from django.contrib.auth.models import User
from psiuApp.models import Carona, Estudos, Extracurriculares, ConhecerPessoas, Liga, ParticipaAtividade
from django.contrib.auth import authenticate, login
from datetime import datetime

listaAtividades = ['carona', 'estudos', 'ligas', 'extracurriculares', 'conhecer_pessoas']
nomeAtividade = {'carona': 'Carona', 
                 'estudos': 'Grupo de Estudos', 
                 'ligas': 'Ligas Acadêmicas', 
                 'extracurriculares': 'Atividades Extracurriculares', 
                 'conhecer_pessoas': 'Conhecer Pessoas'}

def tipoAtividadeForm(tipo: str):
    if tipo == 'carona':
        return CaronaModel2Form
    elif tipo == 'estudos':
        return EstudosModel2Form
    elif tipo == 'extracurriculares':
        return ExtracurricularesModel2Form
    elif tipo == 'ligas':
        return LigasModel2Form
    elif tipo == 'conhecer_pessoas':
        return ConhecerPessoasModel2Form
    return None

def tipoAtividadeModel(tipo: str):
    if tipo == 'carona':
        return Carona
    elif tipo == 'estudos':
        return Estudos
    elif tipo == 'extracurriculares':
        return Extracurriculares
    elif tipo == 'ligas':
        return Liga
    elif tipo == 'conhecer_pessoas':
        return ConhecerPessoas
    return None

def get_atividade(pk: int):
    tipos_atividades = [Carona, Liga, Extracurriculares, Estudos, ConhecerPessoas]
    for tipo in tipos_atividades:
        try:
            atividade = tipo.objects.get(pk=pk) 
            return atividade
        except:
            pass
        
    return None

def get_atividade_type(atividade):
    atividade = get_atividade(atividade)
    if type(atividade) == Carona:
        return 'carona'
    if type(atividade) == Estudos:
        return 'estudos'
    if type(atividade) == Extracurriculares:
        return 'extracurriculares'
    if type(atividade) == Liga:
        return 'ligas'
    if type(atividade) == ConhecerPessoas:
        return 'conhecer_pessoas'
    return None

def get_imagem_atividade(tipo: str):
    return 'psiuApp/img/' + tipo + '.png'

def remove_atividades_expiradas():
    atividades = Atividade.objects.all()

    for atividade in atividades:
        datetime_atividade = datetime.combine(atividade.data, atividade.hora)
        if datetime_atividade < datetime.now():
            participantes_atividade = ParticipaAtividade.objects.filter(atividade=atividade)
            for participante in participantes_atividade:
                participante.delete()
            atividade.delete()


# Create your views here.
def home(request): 
    # processamento antes de mostrar a home page 
    return render(request, 'psiuApp/home.html') 

def days_hours_minutes(td):
    return {'dias': td.days, 'horas': td.seconds//3600, 'minutos': (td.seconds//60)%60}

class AtividadeView(View): 
    def get(self, request, pk, *args, **kwargs): 
        
        remove_atividades_expiradas()

        atividade = get_atividade(pk)
        if atividade is None:
            return redirect('psiuApp:homepage')
        
        #Verifica se o usuário participa da atividade
        botaoParticipar = False
        if request.user.is_authenticated:
            usuario_participa = ParticipaAtividade.objects.filter(atividade=Atividade.objects.get(pk=pk), participante=request.user)
            if len(usuario_participa) == 0:
                botaoParticipar = True

        #Lista de participantes
        participantes = ParticipaAtividade.objects.filter(atividade=Atividade.objects.get(pk=pk))
        tipo_atividade = get_atividade_type(atividade)
        
        datetime_atividade = datetime.combine(atividade.data, atividade.hora)

        tempo_ate_atividade = datetime_atividade - datetime.now()
        
        contexto = {'atividade': atividade, 
                    'botaoParticipar': botaoParticipar, 
                    'participantes': participantes, 
                    'tipoAtividade': tipo_atividade,
                    'nomeAtividade': nomeAtividade.get(tipo_atividade, 'Não existente'),
                    'tempoAteAtividade': days_hours_minutes(tempo_ate_atividade),
                    'imagem_atividade': get_imagem_atividade(tipo_atividade)}

        return render( 
            request,  
            'psiuApp/atividade.html',  
            contexto) 

class AtividadeParticipaView(View): 
    def get(self, request, pk, *args, **kwargs):  
        atividade = get_atividade(pk)
        tipo_atividade = get_atividade_type(atividade)

        if atividade is None:
            return HttpResponseRedirect(reverse_lazy("psiuApp:homepage"))
        
        participantes = ParticipaAtividade.objects.filter(atividade=Atividade.objects.get(pk=pk), participante=request.user)

        if len(participantes) == 0:
            if atividade.vagas > 0:
                participacao = ParticipaAtividade(atividade=Atividade.objects.get(pk=pk), participante=request.user)
                participacao.save()

                atividade.vagas -= 1
                atividade.save()
        else:
            atividade.vagas += len(participantes)
            atividade.save()
            for participante in participantes:
                participante.delete()

        return HttpResponseRedirect(reverse_lazy("psiuApp:atividade", args=[pk,]))


class PerfilView(View): 
    def get(self, request, pk, *args, **kwargs): 
        
        #Verifica se esse usuário existe
        try:
            perfil = User.objects.get(pk=pk) 
        except:
            return redirect('psiuApp:homepage')
        
        atividades_criadas = []
        for tipo_atividade in listaAtividades:
            atividades = tipoAtividadeModel(tipo_atividade).objects.filter(criador=pk)
            for atividade in atividades:
                atividade.tipo = tipo_atividade
            atividades_criadas.extend(atividades)
    
        #Pega atividades que usuário participa
        participacoes = ParticipaAtividade.objects.filter(participante=pk)
        atividades_participa = []
        for participa in participacoes:
            atividade = get_atividade(participa.atividade.id)
            atividade.tipo = get_atividade_type(atividade)
            atividades_participa.append(atividade)


        contexto = {'atividades_criadas': atividades_criadas, 'atividades_participa': atividades_participa, 'perfil': perfil,} 

        return render( 
            request,  
            'psiuApp/perfil.html',  
            contexto) 


class AtividadeListView(View): 
    def get(self, request, tipo, *args, **kwargs): 
        
        remove_atividades_expiradas()

        if tipo not in listaAtividades:
            return redirect('psiuApp:homepage') 
        
        atividades = tipoAtividadeModel(tipo).objects.all()
        for atividade in atividades:
            atividade.tipo = tipo

        contexto = { 'atividades': atividades, 'tipoAtividade': tipo, 'nomeAtividade': nomeAtividade.get(tipo, 'Não existente'), 'imagem_atividade': get_imagem_atividade(tipo)} 

        return render( 
            request,  
            'psiuApp/listaAtividades.html',  
            contexto) 

class AtividadeCreateView(LoginRequiredMixin, View): 
    def get(self, request, tipo, *args, **kwargs): 

        if tipo not in listaAtividades:
            return redirect('psiuApp:homepage') 
        
        contexto = { 'formulario': tipoAtividadeForm(tipo), 
                    'tipoAtividade': tipo, 
                    'nomeAtividade': nomeAtividade.get(tipo, 'Não existente'), 
                    'imagem_atividade': get_imagem_atividade(tipo)} 
        
        return render(request, "psiuApp/criaAtividade.html", contexto) 
    
    def post(self, request, tipo, *args, **kwargs):
        formulario = tipoAtividadeForm(tipo)(request.POST)
        if formulario.is_valid():
            atividade = formulario.save()
            atividade.criador = request.user
            atividade.save() 
            return HttpResponseRedirect(reverse_lazy("psiuApp:lista-atividades", args=[tipo,])) 
        else:
            contexto = { 'formulario': formulario, 
                    'tipoAtividade': tipo, 
                    'nomeAtividade': nomeAtividade.get(tipo, 'Não existente'), 
                    'imagem_atividade': get_imagem_atividade(tipo)} 
        
            return render(request, "psiuApp/criaAtividade.html", contexto) 


class AtividadeUpdateView(LoginRequiredMixin, View): 
    def get(self, request, pk, *args, **kwargs):
        tipo_atividade = get_atividade_type(get_atividade(pk))
        atividade = tipoAtividadeModel(tipo_atividade).objects.get(pk=pk) 

        if atividade.criador != request.user:
            return HttpResponseRedirect(reverse_lazy("psiuApp:homepage"))

        formulario = tipoAtividadeForm(tipo_atividade)(instance=atividade)

        context = {'formulario': formulario, 
                   'nomeAtividade': nomeAtividade.get(tipo_atividade, 'Não existente'), 
                   'pk_atividade': pk, 
                   'imagem_atividade': get_imagem_atividade(tipo_atividade)} 
        
        return render(request, 'psiuApp/atualizaAtividade.html', context) 
     
    def post(self, request, pk, *args, **kwargs):
        tipo_atividade = get_atividade_type(get_atividade(pk))
        atividade = get_object_or_404(tipoAtividadeModel(tipo_atividade), pk=pk) 

        if atividade.criador != request.user:
            return HttpResponseRedirect(reverse_lazy("psiuApp:homepage"))
        
        formulario = tipoAtividadeForm(tipo_atividade)(request.POST, instance=atividade) 

        if formulario.is_valid(): 
            atividade = formulario.save() # cria uma pessoa com os dados do formulário 
            atividade.save()        # salva uma pessoa no banco de dados 
            return HttpResponseRedirect(reverse_lazy("psiuApp:atividade", args=[pk,])) 
        else: 
            contexto = {'formulario': formulario, 
                   'nomeAtividade': nomeAtividade.get(tipo_atividade, 'Não existente'), 
                   'pk_atividade': pk, 
                   'imagem_atividade': get_imagem_atividade(tipo_atividade)} 
            return render(request, 'psiuApp/atualizaAtividade.html', contexto) 
        

class AtividadeDeleteView(LoginRequiredMixin, View): 
    def get(self, request, pk, *args, **kwargs): 
        atividade = Atividade.objects.get(pk=pk)

        if atividade.criador != request.user:
            return HttpResponseRedirect(reverse_lazy("psiuApp:homepage"))

        contexto = { 'atividade': atividade, } 
        return render(request, 'psiuApp/apagaAtividade.html', contexto) 
    
    def post(self, request, pk, *args, **kwargs): 
        atividade = Atividade.objects.get(pk=pk) 

        if atividade.criador != request.user:
            return HttpResponseRedirect(reverse_lazy("psiuApp:homepage"))
        tipo_atividade = get_atividade_type(atividade)

        atividade.delete() 
        return HttpResponseRedirect(reverse_lazy("psiuApp:lista-atividades", args=[tipo_atividade,]))

def registro(request): 
    if request.method == 'POST': 
        formulario = UserCreationForm(request.POST) 
        if formulario.is_valid():
            senha = formulario.cleaned_data.get('password1')
            username = formulario.save()
            user = authenticate(request, username=username, password=senha)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy("psiuApp:editar-perfil", args=[user.id,]))
            return redirect('psiuApp:homepage')
        else:
            context = {'form': formulario, } 
            return render(request, 'psiuApp/registro.html', context)
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