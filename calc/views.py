from django.shortcuts import render
#httprespose
from django.http import HttpResponse

#home function -inital path
def home(request):
    #render home.html in the template folder
    return render(request,'home.html',{'name':'Deepak'})