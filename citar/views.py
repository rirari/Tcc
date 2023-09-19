from django.shortcuts import render, get_object_or_404, redirect
from .models import Formas,Funções,Plagio,Sites, Normas

# Create your views here.

def index (request):
    return render(request, 'core/index.html')

def pagina_formas (request):
    formas = Formas.objects.all()
    context = {
        'formas': formas
    }
    return render(request, 'core/formas.html',context)


def pagina_funções (request):
    funções = Funções.objects.all()
    context ={
        'funções': funções
    }
    return render(request, 'core/funcoes.html',context)

def pagina_normas (request):
    normas = Normas.objects.all()
    context ={
        'normas': normas
    }
    return render(request, 'core/normas.html',context)

def pagina_plagio (request):
    plagios = Plagio.objects.all()
    context ={
        'plagios': plagios
    }
    return render(request, 'core/plagio.html',context)

def pagina_sites (request):
    sites = Sites.objects.all()
    context ={
        'sites': sites
    }
    return render(request, 'core/parasabermais.html',context)

def pagina_sobre (request):
    return render(request, 'core/sobre.html')