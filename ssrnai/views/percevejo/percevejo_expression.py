from django.views.generic import DetailView
from ssrnai.models import Database
from ssrnai.models.percevejo.percevejo_expression import Percevejo_Expression
from ssrnai.models.percevejo.percevejo_expression_description import Percevejo_expression_description
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information


class PercevejoExpression(DetailView):
    template_name = 'percevejo/percevejo_expression.html'
    context_object_name = 'iscore'
    model = Percevejo_Expression
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PercevejoExpression, self).get_context_data(**kwargs)
        context['expression'] = Percevejo_Expression.objects.get(id=int(self.kwargs['pk']))
        expression = context['expression']
        context['gene'] = Percevejo_Gene_Information.objects.get(id=int(expression.gene_id))
        context['descriptions'] = Percevejo_expression_description.objects.all()
        context['database'] = Database.objects.get(id=int(5))

        return context
