from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def index(request): # call with views.index!
    return HttpResponse("Hello, world. You're at the polls index.")