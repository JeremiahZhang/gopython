# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# Import the Category model
from rango.models import Category
from rango.models import Page

def index(request): # creat one view called indext
    # 传递到 templates/index.html 中的 html 变量
    # top five categories
    category_list = Category.objects.order_by('-likes')[:5] 
    context_dict = {'categories': category_list}
    # 如何传递 就要使用 render
    # 默认路径为 .../templates/
    # render the response and send it back
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    # create a context dict which we can pass 
    # to the template rendering engine.
    context_dict = {}
    
    try:
        # Can we find a category name slug with the given name?
        # If we can't the .get() method raise a DoesNotExist exception.
        # So the .get() method returns one model instance or raise an exception.
        category = Category.objects.get(slug=category_name_slug)
        
        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)
        
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didnot find the specified category.
        # Do not do anything -
        # the template will display the 'no category' message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
    
    # Go Render the response and return it to the client.
    return render(request, 'rango/category.html', context_dict)