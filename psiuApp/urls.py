from django.urls.conf import path 
from psiuApp import views 
 
app_name = "psiuApp"

urlpatterns = [ 
    path('listaAtividades/', views.AtividadeListView.as_view(),  
        name='lista-atividades'), 
    path('', views.AtividadeListView.as_view(),  
        name='home'), 
] 