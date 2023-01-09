from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('teste home')

def paginaExterna(request):
    return render(request, 'cadastro/tela inicial.html')