# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'lewis/home.html')