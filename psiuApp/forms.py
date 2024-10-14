from django import forms 
from psiuApp.models import Carona, Extracurriculares, Estudos, Liga, ConhecerPessoas
widgets_data_hora = { 
            'data': forms.TextInput(attrs={'type': 'date',}, ),
            'hora': forms.TextInput(attrs={'type': 'time',}, ),
        }

class CaronaModel2Form(forms.ModelForm):
    class Meta:
        model = Carona 
        exclude = ['criador',]
        widgets = widgets_data_hora
        
class ExtracurricularesModel2Form(forms.ModelForm):
    class Meta:
        model = Extracurriculares 
        exclude = ['criador',]
        widgets = widgets_data_hora

class EstudosModel2Form(forms.ModelForm):
    class Meta:
        model = Estudos 
        exclude = ['criador',]
        widgets = widgets_data_hora

class LigasModel2Form(forms.ModelForm):
    class Meta:
        model = Liga 
        exclude = ['criador',]
        widgets = widgets_data_hora

class ConhecerPessoasModel2Form(forms.ModelForm):
    class Meta:
        model = ConhecerPessoas 
        exclude = ['criador',]
        widgets = widgets_data_hora