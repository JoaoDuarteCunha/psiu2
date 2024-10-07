from django.urls import reverse_lazy
from django.urls.conf import path 
from psiuApp import views 
from django.contrib.auth.views import LoginView, LogoutView

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
] 