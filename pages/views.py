from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    my_context={
        "my_text": 'this is about us',
        "my_number": 123
    }
    return render(request, "home.html", my_context) 

def base_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request, "base.html", {}) 