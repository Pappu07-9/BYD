from cgi import test
from genericpath import exists
from django.forms import NullBooleanField
from django.shortcuts import render, redirect
from .models import Masterdata
from testdrive.models import Testdrive
from booking.models import Booking

# Create your views here.

def saleshome(request):
    datas = Masterdata.objects.all()
    alldatas = [[datas, range(1, len(datas))], ]
    params = {"alldatas": alldatas}
    return render(request, "sales/saleshome.html", params)

def adddata(request):
    return render(request, "sales/adddata.html")

def insert(request):
    if request.method == 'POST':
        userid = request.POST['userid']
        nameofcust = request.POST['name_of_customer']
        address = request.POST['address_of_customer']
        number = request.POST['number_of_customer']
        modelcar = request.POST['interested_model']
        refrence = request.POST['reference']
        status = request.POST['status']
        # followdate = request.POST['followup_date']
        lead_by = request.POST['lead_by']
        bookstatus = request.POST['book_status']
        if bookstatus == 'yes':
            bookstatus = True
        elif bookstatus == 'no':
            bookstatus = False
        testdrive = request.POST['test']
        if testdrive == 'yes':
            testdrive = True
        elif testdrive == 'no':
            testdrive = False

        
        if bookstatus == True and testdrive == True:
            newInq = Masterdata.objects.create(name_of_customer=nameofcust, address_of_customer=address, number_of_customer=number,
                         reference=refrence, interested_model=modelcar, lead_by=lead_by, status=status,book_status=bookstatus, test_drive=testdrive, usertracker=userid)
            newInq.save()
            test = Testdrive.objects.create(name_of_customer=nameofcust, address_of_customer=address, number_of_customer=number,
                         reference=refrence, interested_model=modelcar, lead_by=lead_by, status=status,
                        #  follow_update=followdate,
                         book_status=bookstatus, test_drive=testdrive,usertracker=userid)
            test.save()
            book = Booking.objects.create(name_of_customer=nameofcust, address_of_customer=address, number_of_customer=number,
                         reference=refrence, interested_model=modelcar, lead_by=lead_by, status=status,
                        #  follow_update=followdate,
                         book_status=bookstatus, test_drive=testdrive,usertracker=userid)
            book.save()
            return redirect('saleshome')
        elif testdrive == True:
            newInq = Masterdata.objects.create(name_of_customer=nameofcust, address_of_customer=address, number_of_customer=number,
                         reference=refrence, interested_model=modelcar, lead_by=lead_by, status=status,
                        #  follow_update=followdate,
                         book_status=bookstatus, test_drive=testdrive,usertracker=userid)
            newInq.save()
            test = Testdrive.objects.create(name_of_customer=nameofcust, address_of_customer=address, number_of_customer=number,
                         reference=refrence, interested_model=modelcar, lead_by=lead_by, status=status,
                        #  follow_update=followdate,
                         book_status=bookstatus, test_drive=testdrive,usertracker=userid)
            test.save()
            return redirect('saleshome')
        elif bookstatus == True:
            newInq = Masterdata.objects.create(name_of_customer=nameofcust, address_of_customer=address, number_of_customer=number,
                         reference=refrence, interested_model=modelcar, lead_by=lead_by, status=status,
                        #  follow_update=followdate,
                         book_status=bookstatus, test_drive=testdrive,usertracker=userid)
            newInq.save()
            book = Booking.objects.create(name_of_customer=nameofcust, address_of_customer=address, number_of_customer=number,
                         reference=refrence, interested_model=modelcar, lead_by=lead_by, status=status,
                        #  follow_update=followdate,
                         book_status=bookstatus, test_drive=testdrive,usertracker=userid)
            book.save()
            return redirect('saleshome') 
        newInq = Masterdata.objects.create(name_of_customer=nameofcust, address_of_customer=address, number_of_customer=number,
                         reference=refrence, interested_model=modelcar, lead_by=lead_by, status=status,
                        #  follow_update=followdate,
                         book_status=bookstatus, test_drive=testdrive,usertracker=userid)
        newInq.save()
        print('successful insert')
        return redirect('saleshome')
    
def editdata(request, id):
    data = Masterdata.objects.get(Id=id)
    alldatas = {'data': data, 'id':id}
    return render(request, "sales/editdata.html", alldatas)

def deletedata(request, id):
    data = Masterdata.objects.get(Id=id)
    data.delete()
    
        
    return redirect('saleshome')

#used to update value in database
def update_edit(request, id):
    if request.method == 'POST':
        data = Masterdata.objects.get(Id=id)

        nameofcust = request.POST['updatedname']
        address = request.POST['updatedadd']
        number = request.POST['updatednumber']
        modelcar = request.POST['updatedinterest']
        refrence = request.POST['updatedreference']
        status = request.POST['updatedstatus']
        lead_by = request.POST['updatedlead']
        testdrive = request.POST['updatedtest']
        userid = request.POST['userid']
        if testdrive == 'yes':
            testdrive = True
        elif testdrive == 'no':
            testdrive = False
        else:
            testdrive = False
        bookstatus = request.POST['updatedbookstatus']
        if bookstatus == 'yes':
            bookstatus = True
        elif bookstatus == 'no':
            bookstatus = False
        else:
            bookstatus = False
        data.usertracker = userid
        data.name_of_customer = nameofcust
        data.address_of_customer = address
        data.number_of_customer = number
        data.interested_model = modelcar
        data.reference = refrence
        data.status = status
        data.lead_by = lead_by
        data.test_drive = testdrive
        data.book_status = bookstatus
        data.save()
        return redirect("saleshome")