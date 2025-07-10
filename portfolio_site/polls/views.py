from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse('hi')

def login(request):
    return render(request, "polls/login.html")