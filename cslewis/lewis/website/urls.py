# -*- coding: utf-8 -*-

from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'), 
]