from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Eduardo Igor',
    })

def contato(request):
    return render(request, 'me-apague/temp.html')

def sobre(request):
    return HttpResponse('sobre')
