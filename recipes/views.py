from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('HOME')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')
