from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("Welcome to the Home Page")
    info = {
        "title" : "Portfolio Demo",
        "header" : "Demo App"
    }
    return render(request,'index.html',info)

def AboutUs(request):
    info = {
        "title" : "About us",
        "header" : "About Demo"
    }
    return render(request,'about.html',info)

def AboutAdmin(request,adminName):
    # return HttpResponse(adminName)
    data = {
        "title":adminName,
        "header":"Admin     "+adminName
    }
    return render(request,'aboutAdmin.html',data)

def Services(request):
    info = {
        "title" : "Services",
        "header" : "Service Demo"
    }
    return render(request,'services.html',info)

def Blog(request):
    info = {
        "title" : "Blog",
        "header" : "Blog Demo"
    }
    return render(request,'blog.html',info)

def Contact(request):
    fullName = ""
    try:
        if request.method == "GET":
            # fname = request.GET['firstName']
            fname = request.GET.get('firstName')
            lname = request.GET['lastName']
            email = request.GET['email']
            num = request.GET['number']
            msg = request.GET['userMessage']
            print("=============User : ",fname+lname,"===================")
            fullName = fname +" "+ lname
    except:
        # print("Error")
        pass
    info = {
            "title" : "Contact",
            "header" : "Contact Demo",
            "fullName":fullName
        }
    return render(request,'contact.html',info)

def UserForm(request):
    fullName = ""
    try:
        if request.method == "POST":
            
            # fname = request.POST['firstName']
            fname = request.POST.get('firstName')
            lname = request.POST['lastName']
            email = request.POST['email']
            num = request.POST['number']
            msg = request.POST['userMessage']
            fullName = fname +" "+ lname
    except:
        pass
    info = {
            "title" : "Contact",
            "header" : "Contact Demo",
            "fullName":fullName,
            "fname":fname,
            # yaha sai baki hi ..8 mint tak dekha hu of post method
        }
    return render(request,'userForm.html',info)