from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def SignupPage(request):
   
    

    return render(request,'signup.html')

def LoginPage(request):
    



    return render(request,'login.html')

def HomePage(request):

    return render(request,'home.html')
