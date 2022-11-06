from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Employee
from django.urls import reverse

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
    # print(context)
    return render(request,'allemp.html',context)


def addemp(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        middlename = request.POST['middlename']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        alt_no = request.POST['alt_no']
        email = request.POST['email']
        blood = request.POST['blood']
        new_emp= Employee(firstname=firstname,lastname=lastname,middlename=middlename,gender=gender,mobile=mobile,alt_no=alt_no,email=email,blood=blood)
        new_emp.save()
        return HttpResponseRedirect(reverse('polls:allemp'))

    if request.method =='GET':
        return render(request,'addemp.html')
    return HttpResponse('An exception occured ! Employee')

def Updateemp(request,id):
    obj = Employee.objects.get(id=17)
    if request.method == 'PUT':
        firstname = request.PUT['firstname']
        middlename = request.PUT['middlename']
        lastname = request.PUT['lastname']
        gender = request.PUT['gender']
        mobile = request.PUT['mobile']
        alt_no = request.PUT['alt_no']
        email = request.PUT['email']
        blood = request.PUT['blood']
        new_emp= Employee(firstname=firstname,middlename=middlename,lastname=lastname,gender=gender,mobile=mobile,alt_no=alt_no,email=email,blood=blood)
        new_emp.save()
        return HttpResponseRedirect(reverse('polls:allemp'))

    if request.method =='GET':
        return render(request,'updateemp.html',{"obj":obj})
    return HttpResponse('An exception occured ! Employee')

def Deleteemp(request,id):
    obj = Employee.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect(reverse("polls:allemp"))