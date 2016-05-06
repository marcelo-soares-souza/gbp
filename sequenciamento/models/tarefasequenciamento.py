from django.db import models
from django.contrib.auth.models import User

from sequenciamento.models.sequenciamento import Sequenciamento


class TarefaSequenciamento(models.Model):
    TAREFAS = (
        ('Definição de amostras', 'Definição de amostras'),
        ('Coleta', 'Coleta'),
        ('Extração de DNA', 'Extração de DNA'),
        ('Análise de qualidade', 'Análise de qualidade'),
        ('Preparo para envio', 'Preparo para envio'),
        ('Envio', 'Envio'),
        ('Outros', 'Outros'),
    )

    STATUS = (
        ('Não Iniciado', 'Não Iniciado'),
        ('Em Execução', 'Em Execução'),
        ('Finalizado', 'Finalizado'),
    )

    sequenciamento = models.ForeignKey(Sequenciamento)

    tarefa = models.CharField(max_length=64, choices=TAREFAS)
    status = models.CharField(max_length=64, choices=STATUS)
    responsavel = models.ForeignKey(User, related_name='responsavel_tarefasequenciamento')
    observacao = models.TextField(null=True, blank=True)

    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True)
    data_atualizado = models.DateTimeField(auto_now=True, blank=True)
    criado_por = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['tarefa']
        verbose_name = 'tarefasequenciamento'
        verbose_name_plural = 'tarefasequenciamentos'

    def get_tarefasequenciamento_detail_url(self):
        return u"/tarefasequenciamento/detail/%i" % self.id

    def get_tarefasequenciamento_update_url(self):
        return u"/tarefasequenciamento/update/%i" % self.id

    def get_tarefasequenciamento_delete_url(self):
        return u"/tarefasequenciamento/delete/%i" % self.id

    def __str__(self):
        return '%s %s' % (self.tarefa, self.sequenciamento.material_biologico)
