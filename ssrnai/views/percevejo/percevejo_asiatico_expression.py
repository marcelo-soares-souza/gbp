from django.views.generic import DetailView
from ssrnai.models import Database, organisms
from ssrnai.models.percevejo.percevejo_asiatico_expression import Percevejo_Asiatico_Expression
from ssrnai.models.percevejo.percevejo_expression_description import Percevejo_expression_description
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information


class PercevejoAsiaticoExpression(DetailView):
    template_name = 'percevejo/percevejo_asiatico_expression.html'
    context_object_name = 'iscore'
    model = Percevejo_Asiatico_Expression
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PercevejoAsiaticoExpression, self).get_context_data(**kwargs)
        context['expression'] = Percevejo_Asiatico_Expression.objects.get(id=int(self.kwargs['pk']))
        expression = context['expression']
        context['gene'] = Percevejo_Gene_Information.objects.get(id=int(expression.gene_id))
        context['descriptions'] = Percevejo_expression_description.objects.filter(organism_id=13)
        context['database'] = Database.objects.get(id=int(5))

        return context
