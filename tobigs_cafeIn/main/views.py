from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return render(request, 'main/main.html', {})


def result(request):

    
    return render(request, 'main/result.html', {})