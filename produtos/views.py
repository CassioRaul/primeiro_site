from django.shortcuts import render
from django.http import HttpResponse

def produtos(resquest):
    return render(resquest, 'produtos/index.html')
