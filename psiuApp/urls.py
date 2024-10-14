from django.urls import reverse_lazy
from django.urls.conf import path 
from psiuApp import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.models import User 

app_name = "psiuApp"

urlpatterns = [
    path('criaAtividade/<str:tipo>', views.AtividadeCreateView.as_view(), name='cria-atividade'),
    path('listaAtividades/<str:tipo>', views.AtividadeListView.as_view(), name='lista-atividades'), 
    path('atualiza/<int:pk>/', views.AtividadeUpdateView.as_view(), name='atualiza-atividade'),
    path('apaga/<int:pk>/', views.AtividadeDeleteView.as_view(), name='apaga-atividade'), 
    path('', views.home, name='homepage'), 
    path('atividade/<int:pk>', views.AtividadeView.as_view(), name='atividade'), 
    path('perfil/<int:pk>', views.PerfilView.as_view(), name='perfil'), 
    path('participa_atividade/<int:pk>', views.AtividadeParticipaView.as_view(), name='participa-atividade'),

    #Autenticação
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='psiuApp/login.html', next_page=reverse_lazy('psiuApp:homepage')), name='login'),
    path('logout_usuario/', views.logout, name='logout_usuario'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('psiuApp:homepage'),), name='logout'),
    path('trocar_senha/', PasswordChangeView.as_view(template_name='psiuApp/trocar_senha.html', success_url=reverse_lazy('psiuApp:trocar_senha_finalizado'),), 
                                                        name='trocar_senha'), 
    path('trocar_senha_finalizado/',PasswordChangeDoneView.as_view(template_name='psiuApp/trocar_senha_finalizado.html', ), name='trocar_senha_finalizado'), 
    path('editar_perfil/<int:pk>/', views.PsiuAppUpdateView.as_view(template_name='psiuApp/editar_perfil.html', 
                                                                   success_url=reverse_lazy('psiuApp:homepage'), model=User, fields=['first_name', 'last_name', 'email',], ), 
                                                                   name='editar-perfil'), 
] 