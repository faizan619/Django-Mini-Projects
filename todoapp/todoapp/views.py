from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {
        "title":"this is Faizan",
        "numbers":[2,4,6,8],
    }
    return render(request,"homepage.html",data)

def aboutUs(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"contact.html")

def resume(request):
    return render(request,"resume.html")