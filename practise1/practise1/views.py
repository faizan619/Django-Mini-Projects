from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

def HomePage(request):
    return HttpResponse("Welcome to Django Programming")