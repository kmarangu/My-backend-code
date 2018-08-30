from django.shortcuts import render
from django.http import HttpResponse
from AppTow.models import Topic, Webpage, AccessRecord, User

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'AppTow/index.html',context=date_dict)

def user(request):
    users_list = User.objects.order_by('first_name')
    first_name_dict = {'user':users_list}
    return render(request,'AppTow/User.html',context=first_name_dict)
