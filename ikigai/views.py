from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import controller

# Create your views here.

def forms(request):
    hability = controller.hability()
    key = controller.generate_key()
    return render(request, 'ikigai_forms.html', {
        'key':key,
        's1':hability['s1'],
        's2':hability['s2'],
        's3':hability['s3'],
        's4':hability['s4'],
        'loop':[num for num in range(35*len(hability))],
        'verification':'true'
    })


def charts(request, key):
    if request.method == 'POST':
        key = request.POST.get('form-key')
        name = request.POST.get('name')
        email = request.POST.get('email')
        ikigai = controller.rank_responses([request.POST.get(obj) for obj in request.POST])
        controller.save_data(name, email, key, ikigai)
        condition = 1
    elif request.method == 'GET':
        client = controller.get_client(key)
        key = client['key']
        name = client['name']
        email = client['email']
        condition = 0
    return render(request, 'charts_ikigai.html', {'Name': name, 'Email': email, 'Key':key, 'Condition':condition})

def query(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        option = request.POST.get('option')
        dic_option = {
            1:'Qual a minha vocação',
            2:'Qual minha profissão ideal',
            3:'Qual a base de minha missão',
            4:'O que eu faço com paixão',
            5:'Qual minha razão de ser'
        }
        option = dic_option[int(option)]
        client = controller.get_client(key)
        data = controller.desconcatenate([
            client['profissao'], 
            client['vocacao'],
            client['missao'], 
            client['paixao']
        ])
        my_profile = controller.calculate_profile(data, option)
        return render(request, 'query.html', {'profile':my_profile})

def email(request):
    my_list = [request.POST.get(obj) for obj in request.POST]
    my_list.append(request.get_host())
    controller.send_mail(my_list)
    return HttpResponse('E-mail enviado!')

