from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request): # creat one view called indext
    html = "<html><body>Rango says Tango with Django!</body><br/><a href='/rango/about'>About</a></html>"
    return HttpResponse(html)

def about(request):
    html = "<html><body>Hello, Rango says here is the about page!</body><br/><a href='/'>Index</a></html>"
    return HttpResponse(html)