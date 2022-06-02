#import path
from django.urls import path
#import views
from . import views

#specify mappings
urlpatterns=[
    #initial path
    path('',views.home,name='home'),
    #add path --> which get the data
    path('add',views.add,name='add')

]