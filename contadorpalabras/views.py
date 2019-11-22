from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter 

def homepage(request):
	return render(request, 'home.html')

def contador(request):
	texto_completo = request.GET['texto_ingresado']
	
	palabras = Counter(texto_completo.split())
	frecuencia = {}
	for pal in palabras:
		frecuencia[pal]=palabras[pal]

	return render(request, 'contador.html', {'texto_completo': texto_completo, 'cantidad': len(palabras), 'palabra_frecuencia': frecuencia})