from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs   ):
    return render(request, 'home.html', {})
    # return HttpResponse("<h1>Hi {0}</h1>".format(request.user))

def category_view(request, *args, **kwargs):
    return render(request, 'category.html', {})