from django.shortcuts import render
#httprespose
from django.http import HttpResponse

#home function -inital path
def home(request):
    #render home.html in the template folder
    return render(request,'home.html',{'name':'Deepak'})

#add function
def add(request):
    #fetch the values
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])

    res = val1+val2
    #render result.html 
    return render(request,'result.html',{'result':res})