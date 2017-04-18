from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request): # creat one view called indext
    return HttpResponse("Rango says Tango with Django!")

def about(request):
    return HttpResponse("Hello, Rango says here is the about page.")