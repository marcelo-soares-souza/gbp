from django.views.generic import DetailView
from ssrnai.models.conyza.conyza_expression import Conyza_Expression
from ssrnai.models.conyza.conyza_expression_description import Conyza_expression_description
from ssrnai.models.conyza.conyza_gene_information import Conyza_Gene_Information


class BuvaExpression(DetailView):
    template_name = 'buva/buva_expression.html'
    context_object_name = 'expression'
    model = Conyza_Expression
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(BuvaExpression, self).get_context_data(**kwargs)
        context['expression'] = Conyza_Expression.objects.get(id=int(self.kwargs['pk']))
        expression = context['expression']
        context['gene'] = Conyza_Gene_Information.objects.get(id=int(expression.gene_id))
        context['descriptions'] = Conyza_expression_description.objects.all()

        return context
