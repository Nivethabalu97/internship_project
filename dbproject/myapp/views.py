from django.http import HttpResponseRedirect
from django.shortcuts import render
from myapp import forms

# Create your views here.
from django.urls import reverse

from myapp.models import Student, Employee,Emp


def home(request):
    return render(request,'testhome.html')

def studetails(request):
    return render(request,'studentadd.html')

def addstudentdetails(request):
    sname=request.POST['sname']
    sage = request.POST['sage']
    smark = request.POST['smark']
    stype = request.POST['stype']
    obj1=Student(age=sage,name=sname,marks=smark,stype=stype)
    obj1.save()
    return render(request,'studentadd.html',{'output':'data inserted successfully'})

def empdetails(request):
    return render(request,'empadd.html')

def addempdetails(request):
    ename=request.POST['name']
    eage = request.POST['age']
    position = request.POST['position']
    years = request.POST['years']
    obj1=Employee(name=ename,age=eage,position=position,years=years)
    obj1.save()

    eobj1=Employee.objects.filter(name='karthick')
    return render(request,'empadd.html',{'output':'data inserted successfully','myobj':eobj1})

def test(request):
    return render(request,'testhome.html')

def aboutus(request):
    return render(request,'aboutus.html')

def addemp(request):
    return render(request,'emadd.html')

def addem(request):
    empname=request.POST['ename']
    empage = request.POST['eage']
    position = request.POST['eposition']
    gender = request.POST['egender']
    object1=Emp(name=empname,age=empage,position=position,gender=gender)
    object1.save()
    return render(request,'emadd.html',{'output':'data inserted successfully','myobj':object1})

def viewem(request):
    obj = Emp.objects.all()
    return render(request, 'viewem.html', {'output': 'data inserted successfully', 'myobj': obj})

def delemp(request,id):
    delemp= Emp.objects.get(id=id)
    delemp.delete()
    return HttpResponseRedirect(reverse('viewem'))

def filterdetails_copy(request):
    menu = Emp.objects.values_list('emp_roll')
    menu_list = []
    for item in menu:
        for j in item:
            conv_type = f"{j}"
            num_type = int(conv_type)
            menu_list.append(num_type)
    return render(request,'filteremp.html',{'menu':menu_list})

def filterdetails(request):
    obj1=Emp.objects.all()
    return render(request, 'filteremp.html', {'dropdown': obj1})

def filterfun(request):

    name=request.POST['roll']
    mydata = Emp.objects.filter(emp_roll=name).values()

    return render(request,'filteremp.html',{'records':mydata})

def mymaster(request):
    return render(request, 'child.html')

def mymaster1(request):
    return render(request, 'child1.html')

def getForm(request):
    frontform=forms.myForm();
    return render(request,'register.html',{"frontform":frontform})

def register(request):
     return render(request,'registeration.html')


def login(request):
    return render(request, 'login.html')