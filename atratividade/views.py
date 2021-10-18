from django.shortcuts import render
from django.urls import include
from django.http import HttpResponse 


# Create your views here.


def home(request):
    questions = [
        'Ninguém aguenta mais o termo "cringe"',
        'Eu sou humilde',
        'Volta Domingão do Faustão',
        'Volta Caldeirão',
        'Tio Zuck espião',
        'Flamengo é melhor time',
        'Velozes e furiosos perdeu a graça',
        'The Walking Dead precisa acabar',
        'Sofrencia é bom',
    ]
    return render(request, 'home/index.html', {"questions":questions})