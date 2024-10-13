''' 
Created on 8 de out de 2019 
@author: meslin 
''' 
 
from django import forms 
from psiuApp.models import Carona, Extracurriculares, Estudos, Liga, ConhecerPessoas

class CaronaModel2Form(forms.ModelForm):
    class Meta:
        model = Carona 
        fields = '__all__'

class ExtracurricularesModel2Form(forms.ModelForm):
    class Meta:
        model = Extracurriculares 
        fields = '__all__'

class EstudosModel2Form(forms.ModelForm):
    class Meta:
        model = Estudos 
        fields = '__all__'

class LigasModel2Form(forms.ModelForm):
    class Meta:
        model = Liga 
        fields = '__all__'

class ConhecerPessoasModel2Form(forms.ModelForm):
    class Meta:
        model = ConhecerPessoas 
        fields = '__all__'