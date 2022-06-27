from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import Plant
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)
        messages.info(request, "Succsefully logined")
        return redirect('/')

    return render(request,"login.html")

def register(request):
    return render(request,"register.html")
def plantorder(request):

    return render(request,"plantorder.html")

def fun(request):
    HttpResponse("your order is placed")

def plantdetails(request):

    return render(request,"plantdetails.html")

def shop(request):
    return render(request,"shop.html")



def logout(request):
    auth.logout(request)
    return redirect('/')
