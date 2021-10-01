from django.shortcuts import render
from django.views.generic.base import View
from ssrnai.models import Organisms
from django.views.generic import DetailView


class ShowOrganism(DetailView):

    def post(request):
        context = {}
        organism = request.POST.get('organism')
        #organism = Organisms.objects.filter(id=int(id))

        context['organism'] = organism

        return render(request, 'show-organism.html', context)
    
    #success_url = reverse_lazy('show-organism')
