from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn=input("enter topic")
    TO=Topic.filter(topic_name=tn)
    return HttpResponse("Im created....")
def insert_Webpage(request):
    tn=input("Enter topic name")
    n=input("enter name")
    u=input("enter ur")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse("again IM created.....")

def Access(request):
    #topic_name=input("enter topic name")
    tn=input("enter topic_name")
    u=input("enter url")
    d=input("enter date")
    a=input("enter author")  
    n=input("enter name") 
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    TO.save()
    WO.save()

    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    return HttpResponse("access created..................")
def display_topics(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'topic.html',d)
def display_webpages(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,"webpage.html",d)