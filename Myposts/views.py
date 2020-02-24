from django.shortcuts import render
from . models import event

# Create your views here.

def First(request):

    events=event.objects.all()
    return render(request,'Myposts/First.html',{'events':events})

def Details(request,event_id):
    e=event.objects.get(pk=event_id)
    return render(request,'Myposts/details.html',{'e':e})