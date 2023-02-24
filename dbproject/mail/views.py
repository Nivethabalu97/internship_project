from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings

def viewmail(request):
        return render(request,'mail.html')


def mymail(request):
        if request.method=='POST':
                recipient = request.POST['recipient']
                message= request.POST['message']
                send_mail(message, message,settings.DEFAULT_FROM_EMAIL,[recipient])
                return render(request, 'mail.html',{"status":"successfully sent"})
        else:
                return render(request,'login.html',{"status":"not sent"})
