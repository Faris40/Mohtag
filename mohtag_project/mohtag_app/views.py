from django.shortcuts import render, redirect
from django.http import HttpRequest
from . models import Family, Donation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required



# Create your views here.

def home(request : HttpRequest):

    return render(request, 'home.html')

def about(request : HttpRequest):

    return render(request, 'about.html')


@login_required(login_url='accounts:user_login')
def new_family(request : HttpRequest):
    if not request.user.has_perm("mohtag_app.new_family"):
        return redirect('mohtag_app:no_perm')

    if request.method == 'POST':

        new_family = Family(family_name = request.POST['family_name'],family_dis = request.POST['family_dis'])
        new_family.save()

    return render(request,'new_family.html')


def family(request : HttpRequest):

    family = Family.objects.all()

    return render(request, 'family.html',{'family' : family})


@login_required(login_url='accounts:user_login')
def don(request: HttpRequest):
    if request.method == 'POST':

        new_don = Donation(donation_type = request.POST['donation_type'],donation_dis = request.POST['donation_dis'],donation_cond = request.POST['donation_cond'], donation_phone = request.POST['donation_phone'])
        new_don.save()

    return render(request,'don.html')


    
@login_required(login_url='accounts:user_login')
def view_don(request : HttpRequest):

    if not request.user.has_perm("mohtag_app.new_family"):
        return redirect('mohtag_app:no_perm')

    view_don = Donation.objects.all()

    return render(request, 'view_don.html',{'view_don' : view_don})

def del_don(request : HttpRequest, donation_id : int):

    donation = Donation.objects.get(id = donation_id)

    donation.delete()
    return redirect("mohtag_app:view_don")


def del_family(request : HttpRequest, family_id : int):

    family = Family.objects.get(id = family_id)

    family.delete()
    return redirect("mohtag_app:family")


def no_perm(request : HttpRequest):

    return render(request , 'no_perm.html')        