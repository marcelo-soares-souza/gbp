from django.views.generic import DetailView
from ssrnai.models.lagarta.lagarta_expression import Lagarta_Expression
from ssrnai.models.lagarta.lagarta_expression_description import Lagarta_expression_description
from ssrnai.models.lagarta.lagarta_gene_information import Lagarta_Gene_Information
from ssrnai.models import Database


class LagartaExpression(DetailView):
    template_name = 'lagarta/lagarta_expression.html'
    context_object_name = 'iscore'
    model = Lagarta_Expression
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(LagartaExpression, self).get_context_data(**kwargs)
        context['expression'] = Lagarta_Expression.objects.get(id=int(self.kwargs['pk']))
        expression = context['expression']
        context['gene'] = Lagarta_Gene_Information.objects.get(id=int(expression.gene_id))
        context['descriptions'] = Lagarta_expression_description.objects.all()
        context['database'] = Database.objects.get(id=int(4))

        return context
