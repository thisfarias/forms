from django.shortcuts import redirect, render
from django.urls import include, reverse
from django.http import HttpResponse, HttpResponseRedirect
from . import controller

# Create your views here.

def forms(request):
    question = controller.arguments()
    key = controller.generate_key()
    return render(request, 'forms.html', {"questions":question, 'key':key})

def business_rules(request, key):
        myList = [request.POST.get(obj) for obj in request.POST]
        del myList[0]
        del myList[len(myList)-1]
        profile = controller.profile_category(myList, key)
        return profile
        

def charts(request, key):
    if request.method == 'POST':
        key = request.POST.get('form-key')
        my_list = business_rules(request, key)
        return render(request, 'charts.html', {
                'Name':my_list[0],
                'Email':my_list[1],
                'Organizacao':my_list[2],
                'Tecnica':my_list[3],
                'Comportamental':my_list[4],
                'Empreend':my_list[5],
                'Intra':my_list[6],
                'Lideranca':my_list[7],
                'Total':my_list[8],
                'Key':key,
                'Condition':1
            })
    if request.method == 'GET':
        my_list = controller.get_client(key)
        return render(request, 'charts.html', {
                'Name':my_list[0],
                'Email':my_list[1],
                'Organizacao':my_list[2],
                'Tecnica':my_list[3],
                'Comportamental':my_list[4],
                'Empreend':my_list[5],
                'Intra':my_list[6],
                'Lideranca':my_list[7],
                'Total':my_list[8],
                'Key':key,
                'Condition':0
            })

def email(request):
    my_list = [request.POST.get(obj) for obj in request.POST]
    my_list.append(request.get_host())
    controller.send_mail(my_list)
    return HttpResponse('E-mail enviado!')
