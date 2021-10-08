from django.db.models.fields import CharField
from django.shortcuts import render
from django.views.generic.base import View
from ssrnai.models import Organisms
from django.views.generic import DetailView
from django.db.models import Q
from ssrnai.models.percevejo.percevejo_dsrna_information import Percevejo_Dsrna_Information
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information


class ShowOrganism(DetailView):

    def post(self, request):
        context = {}
        database = request.POST.get('db', '')
        context['database'] = database 
        #if database == 5:
            #Gene = Percevejo_Gene_Information()
            
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
        nextgene = Percevejo_Gene_Information()
        if not not gene:
            try:
                if organism != '0':
                    genes = Percevejo_Gene_Information.objects.filter(gene_name__icontains=gene, organism_id=int(organism))
                    #context['genes'] = genes
                else:
                    genes = Percevejo_Gene_Information.objects.filter(gene_name__icontains=gene)
                    #context['genes'] = genes
            except genes.DoesNotExist:
                nextgene.gene_name = 'Busca retornou 0 genes'
                genes.append(nextgene)
                #context['genes'] = genes

        for g in genes:
            gene_list.append(g)

        #gene function search
        genes = []
        nextgene = Percevejo_Gene_Information()
        if not not gene_function:
            try:
                if organism != '0':
                    genes = Percevejo_Gene_Information.objects.filter(gene_description__icontains=gene_function, organism_id=int(organism))
                    #context['genes'] = genes
                else:
                    genes = Percevejo_Gene_Information.objects.filter(gene_description__icontains=gene_function)
                    #context['genes'] = genes
            except genes.DoesNotExist:
                nextgene.gene_name = 'Busca retornou 0 genes'
                genes.append(nextgene)

        for g in genes:
            gene_list.append(g)

        #GO function search
        genes = []
        nextgene = Percevejo_Gene_Information()
        if not not go_function:
            try:
                if organism != '0':
                    genes = Percevejo_Gene_Information.objects.filter(gene_ontology_blastx__icontains=go_function, organism_id=int(organism))
                    #context['gene_ontology_blastx'] = newgene
                else:
                    genes = Percevejo_Gene_Information.objects.filter(gene_ontology_blastx__icontains=go_function)

            except genes.DoesNotExist:
                nextgene.gene_description = 'Erro go'
                genes.append(nextgene)

        for g in genes:
            gene_list.append(g)

        context['genes'] = gene_list

        


        
        

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

        return render(request, 'show-organism/show-organism.html', context)
    
    #success_url = reverse_lazy('show-organism')
