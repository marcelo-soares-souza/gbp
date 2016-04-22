from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

from projeto.models.tipo import Tipo
from projeto.models.status import Status
from projeto.models.instituicao import Instituicao

'''
Classe Modelo de Projeto. Principal classe do sistema, que possui todas as informações de um projeto {seja em atributos e/ou relacionamentos com as outras classes}       
'''

class Projeto(models.Model):
    
    #Atributos
    #Número SEG
    seg = models.CharField(max_length=32, validators=[MinLengthValidator(2)], blank=True)
    titulo_portugues = models.CharField(max_length=256, validators=[MinLengthValidator(5)], blank=True)
    titulo_ingles = models.CharField(max_length=256, validators=[MinLengthValidator(5)], blank=True)
    #Sigla: padrão embrapa - máximo 8 dígitos, upcaser, sem caracteres especiais
    sigla = models.CharField(max_length=32, validators=[MinLengthValidator(2)], blank=True)
    #Data de ínicio do projeto: dd/mm/aaaa
    data_inicio = models.DateField(blank=True)
    #Quando tempo em meses, que o projeto vai durar
    duracao = models.IntegerField(blank=True)
    hipotese = models.TextField(blank=True)
    objetivo_geral = models.TextField(blank=True)
    resumo = models.TextField(blank=True)
    
    #Relacionamentos
    #Tipo de Projeto:cadastrados pelo Adm. Relação: Tipo 1 - * Projeto
    tipo = models.ForeignKey(Tipo, null=True, blank=True, related_name='tipo')
    
    #Status do Projeto: cadastrados pelo Adm. Relação: Status 1 - * Projeto
    status = models.ForeignKey(Status, null=True, blank=True, related_name='status')
    
    #Líder: são os usuários cadastrados no sistema. Relação: Líder 1 - * Projeto
    lider = models.ForeignKey(User, null=True, blank=True, related_name='lider')
    
    #Instituição: podem ser proponentes ou executoras. Relação: Instituição 1 - * Projeto
    instituicao_proponente = models.ForeignKey(Instituicao, related_name='proponente', null=True, blank=True)
    instituicao_executora = models.ForeignKey(Instituicao, related_name='executora', null=True, blank=True)
    
    
    #Projeto relacionado: é um auto-relacionamento, uma vez que um projeto cadastrado pode estar relacionado com outro. Projeto Relacionado 1 - * Projeto 
    projeto_relacionado = models.ForeignKey('self', related_name='relacionado', null=True, blank=True)
    
       
    #Atributos de Controle/Log
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True, related_name='criado')
    
    
    class Meta:
        ordering = ['sigla']
        verbose_name = 'projeto'
        verbose_name_plural = 'projetos'

    def get_projeto_detail_url(self):
        return u"/detail/%i" % self.id

    def get_projeto_update_url(self):
        return u"/update/%i" % self.id

    def get_projeto_delete_url(self):
        return u"/delete/%i" % self.id
    
    
    def __str__(self):
        return self.sigla
