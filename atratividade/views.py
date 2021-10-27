from django.shortcuts import redirect, render
from django.urls import include, reverse
from django.http import HttpResponse, HttpResponseRedirect
from . import controller

# Create your views here.

def forms(request):
    #return render(request, 'forms.html', {"questions":controller.arguments()})
    question = [
        'Greys Anatomy precisa acabar',
        'Eu sou gostoso',
        'Back-end >>>> Front-end',
        'Em casa de ferreiro, não se olha os dentes',
        'FIAP é facul de milionario',
        'Volta domigão do faustao'
    ]
    return render(request, 'forms.html', {"questions":question})

def business_rules(request):
        myList = [request.POST.get(obj) for obj in request.POST]
        del myList[0]
        profile = controller.profile_category(myList)
        return profile
        

def charts(request):
    if request.method == 'POST':
        my_list = business_rules(request)
        return render(request, 'charts.html', {
                'Name':my_list[0],
                'Email':my_list[1],
                'Organizacao':my_list[2],
                'Tecnica':my_list[3],
                'Comportamental':my_list[4],
                'Empreend':my_list[5],
                'Intra':my_list[6],
                'Lideranca':my_list[7],
                'Total':my_list[8]
            })

def email(request):
    my_list = [request.POST.get(obj) for obj in request.POST]
    controller.send_mail(my_list)
    return HttpResponse('E-mail enviado!')


def test(request):
    return HttpResponse('Olá')