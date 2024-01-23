from django.shortcuts import render
from .models import Testdrive
# Create your views here.
def testdrivehome(request):
     datas = Testdrive.objects.all()
     alldatas = [[datas, range(1, len(datas))], ]
     params = {"alldatas": alldatas}
     return render(request, "testdrive/testdrivehome.html", params)