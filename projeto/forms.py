from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import Instituicao, Objetivo, Resultado, Projeto
from localflavor.br.forms import BRCNPJField, BRPhoneNumberField, BRZipCodeField, BRStateSelect

    
class InstituicaoForm(forms.ModelForm):
    
    cep = BRZipCodeField(label='CEP')
    estado = BRStateSelect()
    telefone = BRPhoneNumberField()
    cnpj = BRCNPJField(label='CNPJ')

    class Meta:
        model = Instituicao
        fields = ('sigla', 'nome', 'site', 'email', 'endereco', 'cidade', 'descricao', 'cnpj', 'telefone', 'estado', 'cep')
        
        widgets = {
            'sigla': TextInput(attrs={'style': 'width: 128px;'}),
            'descricao': Textarea(attrs={'cols': '5', 'rows': '5'}),
        }

        labels = {
            'sigla': 'Sigla',
            'email': 'E-Mail',
            'endereco': 'Endereço',

            'descricao': 'Descrição',
        }
        
        help_texts = {
            'sigla': ('Sigla da Instituição'),
        }
        

class ObjetivoForm(forms.ModelForm):
    
    class Meta:
        model = Objetivo
        fields = ('projeto', 'numero', 'descricao')
       
        widgets = {
            'descricao': Textarea(attrs={'cols': '5', 'rows': '5'}),
        }
        
        labels = {
            'numero': 'Número',
            'descricao': 'Descrição',
        }

class ResultadoForm(forms.ModelForm):
    
    class Meta:
        model = Resultado
        fields = ('projeto', 'numero', 'descricao', 'objetivo')
        
        widgets = {
            'descricao': Textarea(attrs={'cols': '5', 'rows': '5'}),
        }
        
        labels = {
            'numero': 'Número',
            'descricao': 'Descrição',
        }

        
class ProjetoForm(forms.ModelForm):
    
    class Meta:
        model = Projeto
        fields = ('tipo', 'status', 'lider', 'seg', 'titulo_portugues', 'titulo_ingles', 'sigla', 'data_inicio', 'duracao', 'hipotese', 'instituicao_proponente', 'instituicao_executora', 'objetivo_geral', 'resumo') 
        
        widgets = {
            'hipotese': Textarea(attrs={'cols': '5', 'rows': '5'}),
            'objetivo_geral': Textarea(attrs={'cols': '5', 'rows': '5'}),
            'resumo': Textarea(attrs={'cols': '5', 'rows': '5'}),
        }        
                
        labels = {
            'lider': 'Líder',
            'seg': 'Número SEG',
            'titulo_portugues': 'Título em Português',
            'titulo_ingles': 'Título em Inglês',
            'data_inicio': 'Data de Início',
            'duracao': 'Duração',
            'hipotese': 'Hipótese',
            'instituicao_proponente': 'Instituição Proponente',
            'instituicao_executora': 'Instituição Executora',          
        } 

