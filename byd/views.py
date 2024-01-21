from django.shortcuts import render





def index(request):
    return render(request, "homepage/index.html")

def login(request):
    return render(request, "login/login.html")