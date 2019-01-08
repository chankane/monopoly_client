from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(req):
    # return HttpResponse("Hello, World")
    return render(req, 'index.html')
