from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"homepage.html")

def aboutUs(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"contact.html")

def resume(request):
    return render(request,"resume.html")