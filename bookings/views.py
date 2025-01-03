from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def whatIsThis():
    return HttpResponse("this is bookings")
