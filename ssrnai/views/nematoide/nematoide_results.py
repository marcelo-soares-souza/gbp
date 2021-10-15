from django.db.models.fields import CharField
from django.shortcuts import render
from django.views.generic.base import View
from ssrnai.models import Organisms
from django.views.generic import DetailView
from django.db.models import Q
from ssrnai.models.nematoide.nematoide_dsrna_information import Nematoide_Dsrna_Information
from ssrnai.models.nematoide.nematoide_gene_information import Nematoide_Gene_Information
from ssrnai.models.nematoide.nematoide_iscore import Nematoide_Iscore
from ssrnai.models.nematoide.nematoide_dicer import Nematoide_Dicer
from ssrnai.models.nematoide.nematoide_structure import Nematoide_Structure
from ssrnai.models.nematoide.nematoide_expression import Nematoide_Expression
from django.core.exceptions import ObjectDoesNotExist


class NematoideResults(DetailView):

    def post(self, request):
        context = {}
        database = request.POST.get('db', '')
        context['database'] = database 
            
        organism = request.POST.get('organism', '0')
        gene = request.POST.get('gene', '')
        gene_function = request.POST.get('gene_function', '')
        go_function = request.POST.get('go_function', '')
        min_iscore = request.POST.get('min_iscore', '')
        max_iscore = request.POST.get('max_iscore', '')
        min_dicer = request.POST.get('min_dicer', '')
        max_dicer = request.POST.get('max_dicer', '')
        min_structure = request.POST.get('min_structure', '')
        max_structure = request.POST.get('max_structure', '')
        min_expression = request.POST.get('min_expression', '')
        max_expression = request.POST.get('max_expression', '')
        min_ontarget_number = request.POST.get('min_ontarget_number', '')
        max_ontarget_number = request.POST.get('max_ontarget_number', '')
        #organism = Organisms.objects.filter(id=int(id))

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
        nextgene = Nematoide_Gene_Information()

        if not not gene:
            try:
                if organism != '0':
                    genes = Nematoide_Gene_Information.objects.filter(gene_name__icontains=gene, organism_id=int(organism))
                    #context['genes'] = genes
                else:
                    genes = Nematoide_Gene_Information.objects.filter(gene_name__icontains=gene)
                    #context['genes'] = genes
            except ObjectDoesNotExist:
                genes = []

        for g in genes:
            gene_list.append(g)

        #gene function search
        genes = []
        nextgene = Nematoide_Gene_Information()
        if not not gene_function:
            try:
                if organism != '0':
                    genes = Nematoide_Gene_Information.objects.filter(gene_description__icontains=gene_function, organism_id=int(organism))
                    #context['genes'] = genes
                else:
                    genes = Nematoide_Gene_Information.objects.filter(gene_description__icontains=gene_function)
                    #context['genes'] = genes
            except ObjectDoesNotExist:
                genes = []

        for g in genes:
            gene_list.append(g)
        
        genes = list(set(gene_list))
        gene_list = genes

        #GO function search
        genes = []
        nextgene = Nematoide_Gene_Information()
        if not not go_function:
            try:
                if organism != '0':
                    genes = Nematoide_Gene_Information.objects.filter(gene_ontology_blastx__icontains=go_function, organism_id=int(organism))
                    #context['gene_ontology_blastx'] = newgene
                else:
                    genes = Nematoide_Gene_Information.objects.filter(gene_ontology_blastx__icontains=go_function)

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
            try:
                expression = Nematoide_Expression.objects.filter(gene=int(g.id))
            except ObjectDoesNotExist:
                expression = []
            if(len(expression)>1):
                expression = expression[0]

            dsRNAs = []
            try:
                dsRNAs = Nematoide_Dsrna_Information.objects.filter(gene=int(g.id))
                    #context['gene_ontology_blastx'] = newgene
            except ObjectDoesNotExist:
                dsRNAs = []

            result = []
            if not not dsRNAs:
                for ds in dsRNAs:
                    iscore = []
                    try:
                        iscore = Nematoide_Iscore.objects.filter(dsrna=int(ds.id))
                    except ObjectDoesNotExist:
                        iscore = []
                    
                    if(len(iscore)>1):
                        iscore = iscore[0]

                    dicer = []
                    try:
                        dicer = Nematoide_Dicer.objects.filter(dsrna=int(ds.id))
                    except ObjectDoesNotExist:
                        dicer = []

                    if(len(dicer)>1):
                        dicer = dicer[0]
                    
                    estrutura = []
                    try:
                        estrutura = Nematoide_Structure.objects.filter(dsrna=int(ds.id))
                    except ObjectDoesNotExist:
                        estrutura = []

                    if(len(estrutura)>1):
                        estrutura = estrutura[0]

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
                        result.append(iscore.id) #9
                        result.append(iscore.mean_dsir) #10
                        result.append(iscore.mean_iscore) #11
                        result.append(iscore.mean_sbiopredsi) #12
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
                result_list.append(result)


        context['dsRNAs'] = ds_list
        context['result_list'] = result_list    

        #context['min_iscore'] = min_iscore
        #context['max_iscore'] = max_iscore
        #context['min_dicer'] = min_dicer
        #context['max_dicer'] = max_dicer
        #context['min_structure'] = min_structure
        #context['max_structure'] = max_structure
        #context['min_expression'] = min_expression
        #context['max_expression'] = max_expression
        #context['min_ontarget_number'] = min_ontarget_number
        #context['max_ontarget_number'] = max_ontarget_number

        return render(request, 'nematoide/nematoide_results.html', context)
    
    #success_url = reverse_lazy('show-organism')
