from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"baruto/index.html")

def greet(request,name):
    return render(request,"baruto/greet.html",{
        "name":name.capitalize()
    })
