from django.views.generic import DetailView
from ssrnai.models.nematoide.nematoide_expression import Nematoide_Expression
from ssrnai.models.nematoide.nematoide_expression_description import Nematoide_expression_description
from ssrnai.models.nematoide.nematoide_gene_information import Nematoide_Gene_Information
from ssrnai.models import Database

class NematoideExpression(DetailView):
    template_name = 'nematoide/nematoide_expression.html'
    context_object_name = 'expression'
    model = Nematoide_Expression
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(NematoideExpression, self).get_context_data(**kwargs)
        context['expression'] = Nematoide_Expression.objects.get(id=int(self.kwargs['pk']))
        expression = context['expression']
        context['gene'] = Nematoide_Gene_Information.objects.get(id=int(expression.gene_id))
        context['descriptions'] = Nematoide_expression_description.objects.all()
        context['database'] = Database.objects.get(id=int(3))

        return context
