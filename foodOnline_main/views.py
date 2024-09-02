from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse

def home(request):
    return render(request, "home.html")