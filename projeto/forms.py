from django import forms
from django.forms import Textarea, TextInput

from localflavor.br.forms import BRCNPJField,  BRStateSelect, BRZipCodeField
from phonenumber_field.modelfields import PhoneNumberField

from .models import Atividade, Instituicao, MetaProjeto, Objetivo, PalavraChave, PlanoAcao, Projeto, ProjetoComponente, Resultado, Tarefa


class InstituicaoForm(forms.ModelForm):

    cep = BRZipCodeField(label='CEP')
    estado = BRStateSelect()
    telefone = PhoneNumberField()
    cnpj = BRCNPJField(label='CNPJ')

    class Meta:
        model = Instituicao
        fields = ('sigla', 'nome', 'site', 'email', 'endereco',
                  'cidade', 'descricao', 'cnpj', 'telefone', 'estado', 'cep')

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

        '''
        help_texts = {
            'sigla': ('Sigla da Instituição'),
        }
        '''


class ObjetivoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        projetos = kwargs.pop('projetos')
        super(ObjetivoForm, self).__init__(*args, **kwargs)

        try:
            self.initial['projeto'] = Objetivo.objects.latest('data_atualizado').projeto.id
            self.fields['projeto'] = forms.ModelChoiceField(queryset=projetos)
        except Objetivo.DoesNotExist:
            pass

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
    def __init__(self, *args, **kwargs):
        projetos = kwargs.pop('projetos')
        super(ResultadoForm, self).__init__(*args, **kwargs)

        try:
            self.initial['projeto'] = Resultado.objects.latest('data_atualizado').projeto.id
            self.fields['projeto'] = forms.ModelChoiceField(queryset=projetos)
        except Resultado.DoesNotExist:
            pass

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
        fields = ('status', 'lider', 'seg', 'titulo_portugues', 'titulo_ingles', 'sigla', 'data_inicio',
                  'duracao', 'hipotese', 'instituicao_proponente', 'instituicao_executora',
                  'objetivo_geral', 'resumo', 'colaborador', 'jbrowse', 'blast')

        widgets = {
            'hipotese': Textarea(attrs={'cols': '5', 'rows': '5'}),
            'objetivo_geral': Textarea(attrs={'cols': '5', 'rows': '5'}),
            'resumo': Textarea(attrs={'cols': '5', 'rows': '5'}),
        }

        labels = {
            'status': 'Situação',
            'lider': 'Líder',
            'seg': 'Número SEG',
            'titulo_portugues': 'Título em Português',
            'titulo_ingles': 'Título em Inglês',
            'data_inicio': 'Data de Início',
            'duracao': 'Duração',
            'hipotese': 'Hipótese',
            'instituicao_proponente': 'Instituição Proponente',
            'instituicao_executora': 'Instituição Executora',
            'jbrowse': 'JBrowse',
            'blast': 'Blast',
        }


class ProjetoComponenteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        projetos = kwargs.pop('projetos')
        super(ProjetoComponenteForm, self).__init__(*args, **kwargs)

        try:
            self.initial['projeto'] = ProjetoComponente.objects.latest('data_atualizado').projeto.id
            self.fields['projeto'] = forms.ModelChoiceField(queryset=projetos)
        except ProjetoComponente.DoesNotExist:
            pass

    class Meta:
        model = ProjetoComponente
        fields = ('projeto', 'numero', 'nome', 'responsavel')

        labels = {
            'numero': 'Número',
            'responsavel': 'Responsável',
        }


class MetaProjetoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        projetos = kwargs.pop('projetos')
        super(MetaProjetoForm, self).__init__(*args, **kwargs)

        try:
            self.initial['projeto'] = MetaProjeto.objects.latest('data_atualizado').projeto.id
            self.fields['projeto'] = forms.ModelChoiceField(queryset=projetos)
        except MetaProjeto.DoesNotExist:
            pass

    class Meta:
        model = MetaProjeto
        fields = ('projeto', 'numero', 'nome', 'objetivo')

        labels = {
            'numero': 'Número',
        }


class PlanoAcaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        projetos = kwargs.pop('projetos')
        super(PlanoAcaoForm, self).__init__(*args, **kwargs)

        try:
            self.initial['projeto'] = PlanoAcao.objects.latest('data_atualizado').projeto.id
            self.fields['projeto'] = forms.ModelChoiceField(queryset=projetos)
        except PlanoAcao.DoesNotExist:
            pass

    class Meta:
        model = PlanoAcao
        fields = ('projeto', 'projeto_componente', 'numero', 'nome',
                  'responsavel', 'codigo_seg', 'data_inicio', 'data_fim', 'resultado')

        labels = {
            'projeto_componente': 'Projeto Componente',
            'numero': 'Número do PA',
            'nome': 'Nome do PA',
            'responsavel': 'Responsável',
            'codigo_seg': 'Código SEG',
            'data_inicio': 'Data de Início',
            'data_fim': 'Data de Fim',
        }


class AtividadeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        projetos = kwargs.pop('projetos')
        super(AtividadeForm, self).__init__(*args, **kwargs)

        try:
            self.initial['projeto'] = Atividade.objects.latest('data_atualizado').projeto.id
            self.fields['projeto'] = forms.ModelChoiceField(queryset=projetos)
        except Atividade.DoesNotExist:
            pass

    class Meta:
        model = Atividade
        fields = ('projeto', 'planoacao', 'numero', 'nome', 'indicador_fisico',
                  'responsavel', 'peso_planoacao', 'data_inicio', 'data_fim', 'colaborador')

        labels = {
            'planoacao': 'Plano de Ação',
            'numero': 'Número da Atividade',
            'nome': 'Nome da Atividade',
            'indicador_fisico': 'Indicador Físico',
            'responsavel': 'Responsável pela Atividade',
            'peso_planoacao': 'Peso no Plano de Ação',
            'data_inicio': 'Data de Início',
            'data_fim': 'Data de Fim',
            'colaborador': 'Colaboradores da Atividade',
        }


class TarefaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        projetos = kwargs.pop('projetos')
        super(TarefaForm, self).__init__(*args, **kwargs)

        try:
            self.initial['projeto'] = Tarefa.objects.latest('data_atualizado').projeto.id
            self.fields['projeto'] = forms.ModelChoiceField(queryset=projetos)
        except Tarefa.DoesNotExist:
            pass

    class Meta:
        model = Tarefa
        fields = ('projeto', 'planoacao', 'atividade', 'numero', 'nome',
                  'indicador_fisico', 'responsavel', 'peso_atividade', 'colaborador')

        labels = {
            'planoacao': 'Plano de Ação',
            'numero': 'Número da Tarefa',
            'nome': 'Nome da Tarefa',
            'indicador_fisico': 'Indicador Físico',
            'responsavel': 'Responsável pela Atividade',
            'peso_atividade': 'Peso na Atividade',
            'colaborador': 'Colaboradores',
        }


class PalavraChaveForm(forms.ModelForm):

    class Meta:
        model = PalavraChave
        fields = ('projeto', 'palavra')
