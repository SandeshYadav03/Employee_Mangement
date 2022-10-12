from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

def view(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'viewall.html',context)


def allemp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'allemp.html',context)


def addemp(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        middlename = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        alt_no = request.POST['alt_no']
        email = request.POST['email']
        blood = request.POST['blood']
        
        
        new_emp= Employee(firstname=firstname,lastname=lastname,middlename=middlename,gender=gender,mobile=mobile,alt_no=alt_no,email=email,blood=blood)
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method =='GET':
        return  render(request,'addemp.html')
    else:
        return HttpResponse('An exception occured ! Employee')
