from django.shortcuts import render

def index(request):
    return render(request, 'campanha/index.html')

def sobre(request):
    return render(request, 'campanha/sobre.html')

def campanha(request):
    return render(request, 'campanha/campanha.html')

def depoimentos(request):
    return render(request, 'campanha/depoimentos.html')

def contatos(request):
    return render(request, 'campanha/contatos.html')