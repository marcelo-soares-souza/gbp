from django.db.models.fields import CharField
from django.shortcuts import render, get_object_or_404, render_to_response
from django.views.generic.base import View
from ssrnai.models import Organisms, Database, organisms
from django.views.generic import ListView
from django.db.models import Q
from ssrnai.models.conyza.conyza_dsrna_information import Conyza_Dsrna_Information
from ssrnai.models.conyza.conyza_gene_information import Conyza_Gene_Information
from projeto.views.login import LoggedInMixin
from django.urls import reverse_lazy
from ssrnai.models.conyza.conyza_iscore import Conyza_Iscore
from ssrnai.models.conyza.conyza_dicer import Conyza_Dicer
from ssrnai.models.conyza.conyza_structure import Conyza_Structure
from ssrnai.models.conyza.conyza_expression import Conyza_Expression
from ssrnai.models.conyza.conyza_canadensis_expression import Conyza_Canadensis_Expression
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, request


class BuvaResults(ListView):

    allowed_sort_fields = {'gene_name': {'default_direction': '', 'verbose_name': 'Gene_name'},
                           'dsrna_name': {'default_direction': '', 'verbose_name': 'Dsrna_name'}}

    default_sort_field = 'gene_name'

    template_name = 'buva/buva_results.html'
    paginate_by = 10
    context_object_name = 'page_obj'
    fields = '__all__'

    success_url = reverse_lazy('buva_results')

    def get(self, request):
        context = {}

        organism = self.request.GET.get('organism', '0')
        gene = self.request.GET.get('gene', '')
        gene_function = self.request.GET.get('gene_function', '')
        go_function = self.request.GET.get('go_function', '')
        min_iscore = self.request.GET.get('min_iscore', '')
        max_iscore = self.request.GET.get('max_iscore', '')
        min_dicer = self.request.GET.get('min_dicer', '')
        max_dicer = self.request.GET.get('max_dicer', '')
        min_structure = self.request.GET.get('min_structure', '')
        max_structure = self.request.GET.get('max_structure', '')
        min_expression = self.request.GET.get('min_expression', '')
        max_expression = self.request.GET.get('max_expression', '')
        min_ontarget_number = self.request.GET.get('min_ontarget_number', '')
        max_ontarget_number = self.request.GET.get('max_ontarget_number', '')

        #organism search
        if organism == '0':   
            neworganism = Organisms()
            neworganism.organism_name = 'Todos os organismos'
            context['organism'] = neworganism
        else:
            context['organism'] = Organisms.objects.get(id=int(organism))

        #gene search
        gene_list = []
        genes = []
        nextgene = Conyza_Gene_Information()
        #if gene == '*' or gene_function == '*' or go_function == '*':
        #    try:
        #        if organism != '0':
        #            genes = Conyza_Gene_Information.objects.filter(organism_id=int(organism))
        #            #context['genes'] = genes
        #        else:
        #            genes = Conyza_Gene_Information.objects.all()
        #            #context['genes'] = genes
        #    except ObjectDoesNotExist:
        #        genes = []

        if not not gene:
            try:
                if organism != '0':
                    genes = Conyza_Gene_Information.objects.filter(gene_name__icontains=gene, organism_id=int(organism))
                    #context['genes'] = genes
                else:
                    genes = Conyza_Gene_Information.objects.filter(gene_name__icontains=gene)
                    #context['genes'] = genes
            except ObjectDoesNotExist:
                genes = []

        for g in genes:
            gene_list.append(g)

        #gene function search
        genes = []
        nextgene = Conyza_Gene_Information()
        if not not gene_function:
            try:
                if organism != '0':
                    genes = Conyza_Gene_Information.objects.filter(gene_description__icontains=gene_function, organism_id=int(organism))
                    #context['genes'] = genes
                else:
                    genes = Conyza_Gene_Information.objects.filter(gene_description__icontains=gene_function)
                    #context['genes'] = genes
            except ObjectDoesNotExist:
                genes = []

        for g in genes:
            gene_list.append(g)
        
        genes = list(set(gene_list))
        gene_list = genes

        #GO function search
        genes = []
        nextgene = Conyza_Gene_Information()
        if not not go_function:
            try:
                if organism != '0':
                    genes = Conyza_Gene_Information.objects.filter(gene_ontology_blastx__icontains=go_function, organism_id=int(organism))
                    #context['gene_ontology_blastx'] = newgene
                else:
                    genes = Conyza_Gene_Information.objects.filter(gene_ontology_blastx__icontains=go_function)

            except ObjectDoesNotExist:
                genes = []

        for g in genes:
            gene_list.append(g)

        context['genes'] = gene_list

            
        #dsRNA search
        ds_list = []
        result_list = []
        ##cria uma lista de resultado. 
        for g in gene_list:
            expression = []
            if(g.organism_id==8):
                try:
                    expression = Conyza_Canadensis_Expression.objects.filter(gene=int(g.id))
                except ObjectDoesNotExist:
                    expression = []
            else:
                try:
                    expression = Conyza_Expression.objects.filter(gene=int(g.id))
                except ObjectDoesNotExist:
                    expression = []
            
            #if(len(expression)>1):
            #    expression = expression[0]

            dsRNAs = []
            try:
                dsRNAs = Conyza_Dsrna_Information.objects.filter(gene=int(g.id))
                    #context['gene_ontology_blastx'] = newgene
            except ObjectDoesNotExist:
                dsRNAs = []

            result = []
            if not not dsRNAs:
                for ds in dsRNAs:
                    iscore = []
                    try:
                        iscore = Conyza_Iscore.objects.filter(dsrna=int(ds.id))
                    except ObjectDoesNotExist:
                        iscore = []
                    
                    #if(len(iscore)>1):
                    #    iscore = iscore[0]

                    dicer = []
                    try:
                        dicer = Conyza_Dicer.objects.filter(dsrna=int(ds.id))
                    except ObjectDoesNotExist:
                        dicer = []

                    #if(len(dicer)>1):
                    #    dicer = dicer[0]
                    
                    estrutura = []
                    try:
                        estrutura = Conyza_Structure.objects.filter(dsrna=int(ds.id))
                    except ObjectDoesNotExist:
                        estrutura = []

                    #if(len(estrutura)>1):
                    #    estrutura = estrutura[0]

                    result.append(g.id) #0
                    result.append(g.gene_name) #1
                    result.append(g.gene_description) #2
                    result.append(g.gene_ontology_blastx) #3
                    result.append(g.length) #4

                    if not not expression:
                        result.append(expression[0].id) #5
                    else:
                        result.append('-')

                    result.append(ds.dsrna_name) #6
                    localizacao = (str(ds.start) +  '-'  + str(ds.stop)) #NOT A RESULT!!!
                    result.append(localizacao) #7
                    result.append(ds.id) #8

                    if not not iscore:
                        result.append(iscore[0].id) #9
                        result.append(iscore[0].mean_dsir) #10
                        result.append(iscore[0].mean_iscore) #11
                        result.append(iscore[0].mean_sbiopredsi) #12
                    else:
                        result.append("-")
                        result.append("-")
                        result.append("-")
                        result.append("-")

                    if not not dicer:
                        result.append(dicer[0].id) #13
                        result.append(dicer[0].sirna_number) #14
                        result.append(dicer[0].coverage) #15
                    else:
                        result.append("-")
                        result.append("-")
                        result.append("-")

                    if not not estrutura:
                        result.append(estrutura[0].id) #16
                        result.append(estrutura[0].classification) #17
                    else:
                        result.append("-")
                        result.append("-")

                    result.append(str("on_target")) #18
                    result.append(str("off_target")) #19
                    result.append(g.organism_id) #20
                    result_list.append(result)
                    result = []
                    ds_list.append(ds)
            else:
                result.append(g.id) #0
                result.append(g.gene_name) #1
                result.append(g.gene_description) #2
                result.append(g.gene_ontology_blastx) #3
                result.append(g.length) #4
                
                if not not expression:
                    result.append(expression[0].id) #5
                else:
                    result.append('-')

                result.append("-") #6
                result.append("-") #7
                result.append("-") #8
                result.append("-") #9
                result.append("-") #10
                result.append("-") #11
                result.append("-") #12
                result.append("-") #13
                result.append("-") #14
                result.append("-") #15
                result.append("-") #16
                result.append("-") #17
                result.append(str("on_target")) #18
                result.append(str("off_target")) #19
                result.append(g.organism_id) #20
                result_list.append(result)

        page = self.request.GET.get('page', 1)

        paginator = Paginator(result_list, 10)
        
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

        return render(request, 'buva/buva_results.html', { 'results': results })
    
    #success_url = reverse_lazy('show-organism')
