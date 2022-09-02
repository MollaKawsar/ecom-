from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def hellow(request):
    context={}
    return render(request,"index.html", context)

def store(request):
    context={}
    return render(request,"store.html",context)


def SONA_MIA(request):
    context={}
    return render(request,"hello.html",context)