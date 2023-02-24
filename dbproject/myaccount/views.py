from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    return render(request,'registeration.html')

def getregister(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['pwd']

    if User.objects.filter(username=username).exists():
        messages.info(request,'username already exist')
        return redirect('/myaccount/')
    else:
        object1 = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username,password=password)
        object1.save()

        messages.info(request, 'successfully registered')
        return redirect('/myaccount/')

def login(request):
    username = request.POST['username']
    password = request.POST['pwd']
    data = auth.authenticate(username=username,password=password)
    if data is not None:
        auth.login(request,data)
        return render(request,'testhome.html',{'output':data})
    else:
        return render(request, 'login.html', {'output': 'Wrong Credentials'})

def logout(request):
    auth.logout(request)
    return render(request, 'testhome.html',{'result':"Logged out successfully"})




