from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def listado(request):
	#return HttpResponse("Esta es la respuesta")
    return render(request,'productos/paginaEspecial.html')

def categorias(request):
    return render(request,'productos/index.html')
