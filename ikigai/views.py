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
        ikigai = controller.calculate_ikigai(controller.rank_responses([request.POST.get(obj) for obj in request.POST]))
    elif request.method == 'GET':
        pass
    return HttpResponse(ikigai)
