from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else: 
        pass
    return render(request, 'authenticate/login.html', {})

def register_user(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST["username"], request.POST["useremail"], request.POST["password"])
        user.save()
        return redirect('login')
      
    return render(request, "authenticate/register.html")


def homepage(request):
    return HttpResponse("This is member's home.")