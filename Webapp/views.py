from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def Bienvenido(request):
    no_personas = Persona.objects.count()
    personas = Persona.objects.all() #queryset : conjunto de objetos
    context = {'no_personas': no_personas,'personas': personas}
    #context = {'msg1': 'valor mensaje 1','msg2': 'valor mensaje 2'}
    return render(request, template_name='bienvenido.html', context=context)


def Despedida(request):
    return HttpResponse("adios a sitio")
