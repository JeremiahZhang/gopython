# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request): # creat one view called indext
    # 传递到 templates/index.html 中的 html 变量
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    # 如何传递 就要使用 render
    # 默认路径为 .../templates/
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    html = "<html><body>Hello, Rango says here is the about page!</body><br/><a href='/'>Index</a></html>"
    return HttpResponse(html)