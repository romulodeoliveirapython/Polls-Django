from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Olá, Mundo. Você está no index do Polls!')
