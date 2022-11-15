from django.shortcuts import render
from django.http import HttpRequest
from . models import Family, Donation

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



def don(request: HttpRequest):

    return render(request,'don.html')


def new_don(request : HttpRequest):

    if request.method == 'POST':

        new_don = Donation(donation_type = request.POST['donation_type'],donation_dis = request.POST['donation_dis'],donation_cond = request.POST['donation_cond'], donation_phone = request.POST['donation_phone'])
        new_don.save()
    

def view_family(request : HttpRequest):

    view_family = Family.objects.all()

    return render(request, 'view_family.html',{'view_family' : view_family})