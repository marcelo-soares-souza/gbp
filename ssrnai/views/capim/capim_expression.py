from django.views.generic import DetailView
from ssrnai.models.capim.capim_expression import Capim_Expression
from ssrnai.models.capim.capim_expression_description import Capim_expression_description
from ssrnai.models.capim.capim_gene_information import Capim_Gene_Information

class CapimExpression(DetailView):
    template_name = 'capim/capim_expression.html'
    context_object_name = 'iscore'
    model = Capim_Expression
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CapimExpression, self).get_context_data(**kwargs)
        context['expression'] = Capim_Expression.objects.get(id=int(self.kwargs['pk']))
        expression = context['expression']
        context['gene'] = Capim_Gene_Information.objects.get(id=int(expression.gene_id))
        context['descriptions'] = Capim_expression_description.objects.all()

        return context
