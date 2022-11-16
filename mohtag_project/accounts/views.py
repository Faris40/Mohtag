from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def user_register(request : HttpRequest):

    if request.method == 'POST':

        new_user = User.objects.create_user(username= request.POST['username'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], password= request.POST['password'] )
        new_user.save()

    return render(request,'user_register.html')




def user_login(request : HttpRequest):

    if request.method == 'POST':

        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])

        if user : 
            login(request, user)

            return redirect("mohtag_app:home")

    return render(request,'user_login.html')





def charity_register(request : HttpRequest):

    if request.method == 'POST':

        new_user = User.objects.create_user(username= request.POST['username'], first_name = request.POST['first_name'], password= request.POST['password'] )
        new_user.save()

    return render(request,'charity_register.html')
        

    


    

def charity_login(request : HttpRequest):

    return render(request,'charity_login.html')


def user_logout(request : HttpRequest):

    logout(request)

    return redirect('mohtag_app:home')