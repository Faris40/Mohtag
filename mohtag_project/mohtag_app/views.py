from django.shortcuts import render, redirect
from django.http import HttpRequest

# Create your views here.

def home(request : HttpRequest):

    return render(request, 'home.html')

def about(request : HttpRequest):

    return render(request, 'about.html')
