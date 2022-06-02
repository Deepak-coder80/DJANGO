from django.shortcuts import render
#httprespose
from django.http import HttpResponse

#home function
def home(request):
    return HttpResponse('Hello World!!')