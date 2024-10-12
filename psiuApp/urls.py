from django.urls import reverse_lazy
from django.urls.conf import path 
from psiuApp import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.models import User 

app_name = "psiuApp"

urlpatterns = [
    path('cria/', views.AtividadeCreateView.as_view(), name='cria-atividade'),
    path('listaAtividades/', views.AtividadeListView.as_view(), name='lista-atividades'), 
    path('atualiza/<int:pk>/', views.AtividadeUpdateView.as_view(), name='atualiza-atividade'),
    path('apaga/<int:pk>/', views.AtividadeDeleteView.as_view(), name='apaga-atividade'), 
    path('', views.home, name='homepage'), 
    path('segunda/', views.segundaPagina, name='segunda'),

    #Autenticação
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='psiuApp/login.html', next_page=reverse_lazy('psiuApp:homepage')), name='login'),
    path('logout_usuario/', views.logout, name='logout_usuario'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('psiuApp:homepage'),), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='psiuApp/password_change_form.html', success_url=reverse_lazy('psiuApp:password_change_done'),), 
                                                        name='password_change'), 
    path('password_change_done/',PasswordChangeDoneView.as_view(template_name='psiuApp/password_change_done.html', ), name='password_change_done'), 
    path('terminaRegistro/<int:pk>/', views.PsiuAppUpdateView.as_view(template_name='psiuApp/user_form.html', 
                                                                   success_url=reverse_lazy('psiuApp:homepage'), model=User, fields=['first_name', 'last_name', 'email',], ), 
                                                                   name='completaDadosUsuario'), 
] 