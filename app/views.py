from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import SocioTorcedor
from .forms import SocioTorcedorForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'app/home.html')

from django.shortcuts import render

def socio_torcedor(request):
    socios = [
        {'nome': 'João Silva'},
        {'nome': 'Maria Oliveira'},
        {'nome': 'Pedro Santos'},
        {'nome': 'Ana Costa'}
    ]
    
    return render(request, 'app/socio_torcedor.html', {'socios': socios})

def sobre(request):
    return render(request, 'app/sobre.html')

def contato(request):
    return render(request, 'app/contato.html')

@login_required
def home(request):
    return render(request, 'app/home.html')

@login_required
def contato(request):
    return render(request, 'app/contato.html')

@login_required
def sobre(request):
    return render(request, 'app/sobre.html')

@login_required
def socio_torcedor(request):
    return render(request, 'app/socio_torcedor.html')

