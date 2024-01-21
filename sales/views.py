from django.shortcuts import render
from .models import Masterdata

# Create your views here.

def saleshome(request):
    return render(request, "sales/saleshome.html")

def adddata(request):
    return render(request, "sales/adddata.html")

def insert(request):
    if request.method == 'POST':
        nameofcust = request.POST['name_of_customer']
        address = request.POST['address_of_customer']
        number = request.POST['number_of_customer']
        modelcar = request.POST['interested_model']
        refrence = request.POST['reference']
        status = request.POST['status']
        followdate = request.POST['followup_date']
        lead_by = request.POST['lead_by']
        bookstatus = request.POST['book_status']
        if bookstatus == 'yes':
            bookstatus = True
        elif bookstatus == 'no':
            bookstatus = False
        else:
            bookstatus = False
        testdrive = request.POST['test']
        if testdrive == 'yes':
            testdrive = True
        elif testdrive == 'no':
            testdrive = False
        else:
            testdrive = False
        newInq = Masterdata.objects.create(name_of_customer=nameofcust, address_of_customer=address, number_of_customer=number,
                         reference=refrence, interested_model=modelcar, lead_by=lead_by, status=status,follow_update=followdate,
                         book_status=bookstatus, test_drive=testdrive)
        newInq.save()
        print('success')