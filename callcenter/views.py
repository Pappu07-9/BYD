from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from sales.models import Masterdata

User = get_user_model()
# Create your views here.

def callhome(request):
    datas = Masterdata.objects.all()

    alldatas = [[datas, range(1, len(datas))], ]
    params = {"alldatas": alldatas}
    return render(request, 'callcenter/callhome.html',params)

def startcall(request):
    datas = Masterdata.objects.all()
    counter = 0
    alldatas = [[datas, range(1, len(datas))],[counter] ]
    params = {"alldatas": alldatas}
    return render(request,"callcenter/startcall.html",params)