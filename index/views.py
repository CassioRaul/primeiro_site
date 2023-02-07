from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("VOCÊ ESTÁ NO INDEX DO APP!")
