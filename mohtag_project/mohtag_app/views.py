from django.shortcuts import render
from django.http import HttpRequest
from . models import Family

# Create your views here.

def home(request : HttpRequest):

    return render(request, 'home.html')

def about(request : HttpRequest):

    return render(request, 'about.html')



def new_family(request : HttpRequest):

    if request.method == 'POST':

        new_family = Family(family_name = request.POST['family_name'],family_dis = request.POST['family_dis'])
        new_family.save()

    return render(request,'new_family.html')


def family(request : HttpRequest):

    family = Family.objects.all()

    return render(request, 'family.html',{'family' : family})

    
