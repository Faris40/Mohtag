from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def user_register(request : HttpRequest):

    return render(request,'user_register.html')




def user_login(request : HttpRequest):

    return render(request,'user_login.html')



def charity_register(request : HttpRequest):

    return render(request,'charity_register.html')
    

def charity_login(request : HttpRequest):

    return render(request,'charity_login.html')