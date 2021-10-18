from django.shortcuts import render
from django.urls import include
from django.http import HttpResponse 
from . import controller    


# Create your views here.

def forms(request):
    questions = [
        'Ninguém aguenta mais o termo "cringe"',
        'Volta Domingão do Faustão',
        'Tio Zuck espião',
        'Flamengo é melhor time',
        'Velozes e furiosos perdeu a graça',
        'The Walking Dead precisa acabar',
        'Sofrencia é bom',
    ]
    return render(request, 'forms.html', {"questions":questions})