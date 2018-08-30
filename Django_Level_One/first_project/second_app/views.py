from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return  HttpResponse("Hello world")
    my_dict = {'insert_me':"Hello I am from views.py stored in Second_app/help.html"}
    return render(request, 'second_app/help.html', context=my_dict)
