from datetime import datetime
from django import forms 
from psiuApp.models import Carona, Extracurriculares, Estudos, Liga, ConhecerPessoas


widgets_data_hora = { 
            'data': forms.TextInput(attrs={'type': 'date',}, ),
            'hora': forms.TextInput(attrs={'type': 'time',}, ),
        }

def clean_generico(self):
    data = self.cleaned_data.get('data')
    hora = self.cleaned_data.get('hora')
    
    datetime_atividade = datetime.combine(data, hora)
    if datetime_atividade < datetime.now():
        if data < datetime.now().date():
            self._errors['data'] = self.error_class([
                'O evento não pode já ter ocorrido!'])
        else:
            self._errors['hora'] = self.error_class([
                'O evento não pode já ter ocorrido!'])

    return self.cleaned_data


class CaronaModel2Form(forms.ModelForm):
    class Meta:
        model = Carona 
        fields = ['localSaida','localChegada','data','hora','vagas','adicionais']
        widgets = widgets_data_hora

    def clean(self):
        super(CaronaModel2Form, self).clean()
        return clean_generico(self)
        

class ExtracurricularesModel2Form(forms.ModelForm):
    class Meta:
        model = Extracurriculares 
        fields = ['atividade','local','data','hora','vagas','adicionais']
        widgets = widgets_data_hora
    
    def clean(self):
        super(ExtracurricularesModel2Form, self).clean()
        return clean_generico(self)

class EstudosModel2Form(forms.ModelForm):
    class Meta:
        model = Estudos 
        fields = ['materia','local','data','hora','vagas','adicionais']
        widgets = widgets_data_hora
    
    def clean(self):
        super(EstudosModel2Form, self).clean()
        return clean_generico(self)

class LigasModel2Form(forms.ModelForm):
    class Meta:
        model = Liga 
        fields = ['nome','local','data','hora','vagas','adicionais']
        widgets = widgets_data_hora
    
    def clean(self):
        super(LigasModel2Form, self).clean()
        return clean_generico(self)

class ConhecerPessoasModel2Form(forms.ModelForm):
    class Meta:
        model = ConhecerPessoas 
        fields = ['atividade','local','data','hora','vagas','adicionais']
        widgets = widgets_data_hora
    
    def clean(self):
        super(ConhecerPessoasModel2Form, self).clean()
        return clean_generico(self)