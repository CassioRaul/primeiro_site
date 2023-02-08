from django.shortcuts import render
from django.http import HttpResponse

def contatos(resquest):
    return render(resquest, 'contatos/index.html')
