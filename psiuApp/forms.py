''' 
Created on 8 de out de 2019 
@author: meslin 
''' 
 
from django import forms 
from psiuApp.models import Atividade 
 
class AtividadeModel2Form(forms.ModelForm): 
    dataHora = forms.DateField( 
        input_formats=['%d/%m/%Y'],  
        label='Data da Atividade', 
        help_text='Data no formato DD/MM/AAAA', 
    ) 
    class Meta: 
        model = Atividade 
        fields = ['adicionais', 'vagas', 'dataHora']

class CaronaModel2Form(AtividadeModel2Form):
    localSaida = forms.DateField( 
        label='Local de saída',
        required=True,
    ) 
    class Meta(AtividadeModel2Form.Meta): 
        fields = ['localSaida', 'localChegada']