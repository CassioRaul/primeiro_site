from django.shortcuts import render
from django.http import HttpResponse

def sobre_nos(resquest):
    return render(resquest, 'sobre_nos/index.html')
