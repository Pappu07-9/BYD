from django.shortcuts import render,redirect





def index(request):
    return render(request, "homepage/index.html")

def login(request):
    return render(request, "login/login.html")

def logout(request):
    return redirect("homepage")