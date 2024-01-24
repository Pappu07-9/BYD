from django.shortcuts import render
from .models import Booking
# Create your views here.
def bookingview(request):
    datas = Booking.objects.all()
    alldatas = [[datas, range(1, len(datas))], ]
    params = {"alldatas": alldatas}
    return render(request, "booking/bookinghome.html", params)


def process(reqeust, id):
    datas = Booking.objects.get(id=id)
    params = {'datas': datas}
    return render(reqeust, 'booking/processindex.html',params)

