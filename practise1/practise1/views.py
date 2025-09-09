from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def HomePage(request):
    # return HttpResponse("Welcome to Django Programming")
    data = {
        "title": "Home",
        "hero": "Welcome to Django Site",
        "sub_hero": "Where Every Code is a AI Enthusiast",
        "username": "Faizan Alam"
    }
    return render(request, "index.html", data)


def MenuPage(request):

    data = {
        "hero": "Programming List",
        "sub_hero": "All the Programming language list",
        "title": "List",
        "username": "Faizan Alam"
    }
    return render(request, "menu.html", data)


def AboutUs(request):
    output = request.GET['output']
    data = {
        "hero": "Learning With the Best",
        "title": "About",
        "username": "Faizan Alam",
        "output":output
    }
    return render(request, "about.html", data)


def ContactUs(request):

    data = {
        "hero": "Contact Admin",
        "sub_hero": "For Any Query Contact the Admin Regarding the Updates",
        "title": "contact",
        "username": "Faizan Alam"
    }
    return render(request, "contact.html", data)


def ContactFormHandling(request):

    if request.method == "POST":
        name = request.POST['name']
        # return HttpResponse(name)
        if(name == ""):
            return HttpResponse("Enter The Name Please")
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        result = {
            "name":name,
            "email":email,
            "subject":subject,
            "message":message
        }
        
        url = "/about/?output={}".format(name)
        return redirect(url)
