from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from sales.models import *

User = get_user_model()
# Create your views here.

def callhome(request):
    datas = Masterdata.objects.all()
    alldatas = [[datas, range(1, len(datas))], ]
    params = {"alldatas": alldatas}
    return render(request, 'callcenter/callhome.html',params)

def startcall(request):
    startcall = get_random_masterdata()
    datas = Masterdata.objects.all().filter(Id=startcall)
    params = {"datas": datas, "startcall": startcall}
    return render(request,"callcenter/startcall.html",params)


def inserts():
    return redirect("inserts")
