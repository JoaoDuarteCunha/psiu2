from django.urls.conf import path 
from psiuApp import views 
 
app_name = "psiuApp"

urlpatterns = [
    path('cria/', views.AtividadeCreateView.as_view(), name='cria-atividade'),
    path('listaAtividades/', views.AtividadeListView.as_view(), name='lista-atividades'), 
    path('atualiza/<int:pk>/', views.AtividadeUpdateView.as_view(), name='atualiza-atividade'),
    path('apaga/<int:pk>/', views.AtividadeDeleteView.as_view(), name='apaga-atividade'), 
    path('', views.home, name='homepage'), 
    path('segunda/', views.segundaPagina, name='segunda'),
] 