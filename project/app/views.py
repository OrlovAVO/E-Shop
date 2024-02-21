from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'app/index.html')


def about(request):
    return render(request, 'app/about.html')
