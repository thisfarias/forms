from django.shortcuts import render

# Create your views here.

def home(request):
    host = request.get_host()
    ikigai = 'http://'+host+'/ikigai/forms'
    atratividade = 'http://'+host+'/atratividade/forms'
    return render(request, 'home.html', {'ikigai':ikigai, 'atratividade':atratividade})

def handler_404(request, exception=None):
    response = render('404.html')
    response.status_code = 404
    return response