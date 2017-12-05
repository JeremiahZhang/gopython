# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# Import the Category model
from rango.models import Category
from rango.models import Page

from rango.forms import CategoryForm
from rango.forms import PageForm

def index(request): # creat one view called indext
    # 传递到 templates/index.html 中的 html 变量
    # top five categories
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages': page_list}
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

def add_category(request):
    form = CategoryForm()
    
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved.
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            return index(request)
        else:
            print(form.errors)
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages(if any).
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    
    form = PageForm
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
            else:
                print(form.errors)
        
    context_dict = {'form': form, 'category': category}
        
    return render(request, 'rango/add_page.html', context_dict)