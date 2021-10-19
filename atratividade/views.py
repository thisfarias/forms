from django.shortcuts import render
from django.urls import include
from django.http import HttpResponse   
from . import controller
import json

# Create your views here.

def forms(request):
    questions = [
        'The Walking Dead precisa acabar',
        'Sofrencia é bom',
    ]
    return render(request, 'forms.html', {"questions":questions})

def calculate_category(request):
    if request.method == 'POST':
        myList = json.loads(request.POST['myList'])
        info = [
            request.POST['name'],
            request.POST['email']
        ]
        profile = controller.profile_category(info, myList)
        return HttpResponse('Teste')

def generate_graphics(request):
    return render(request, 'graphic.html')