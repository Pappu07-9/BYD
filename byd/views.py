from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def index(request):
    return render(request, "homepage/index.html")

def login_page(request):
    return render(request, "login/login.html")

def logout_user(request):
    logout(request)
    return redirect("homepage")

@login_required
def homepage(request):
    return render(request, "userhomepage/index.html")

def authene(request):

    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']

        if User.objects.filter(username = username1).exists():   
            user = authenticate(username = username1, password = password1)
        else:
            user = None

        if user is not None:
            login(request, user)
            return redirect('homepage1')
            
    messages.error(request,"Try Again")        
    return render(request,'login/login.html')