import csv
from ssrnai.models.percevejo.percevejo_gene_information import Percevejo_Gene_Information

with open('/home/doglas/Dropbox/Embrapa/BD/gbp/Euchistus_heros/dsrna_information.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        genes = Percevejo_Gene_Information.objects.filter(gene_name__icontains=row[1])
        print(genes)
