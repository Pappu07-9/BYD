from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate, login
# Create your views here.

def homepage(request):
    if request.method == 'post':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            messages.ERROR(request, 'Invalid Username')
            return redirect('login')
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.ERROR(request, 'Invalid Password')
            return redirect('login')
        else:
            return redirect('adddata')
    return render(request,'login/login.html')
    # return render(request, "userhomepage/index.html")