from django.shortcuts import render,redirect
from .form import Userform
from .models import Ticketsdata
from django.contrib import messages

# Create your views here.

def Submitticket(request):
    if request.method=="POST":
        detail=Userform(request.POST)
        if detail.is_valid():
            saved_ticket=detail.save()
            messages.success(request,f"The request number has been submitted successfully. Ticket number is: {saved_ticket.id}")
            return redirect('raiseticket')
        else:
            messages.error(request,"Please fill out all the mandatory fields")

    u=Userform()

    return render(request,template_name="IT/Ticket.html",context={"u":u})

def Dashboard(request):
    return render(request,template_name="IT/Dash.html")

def Contact(request):
    return render(request,template_name="IT/Contact.html")

def Gettickets(request):
    t=Ticketsdata.objects.all()
    return render(request,template_name="IT/Get.html",context={"t":t})

def Ticketstatus(request):
    t=Ticketsdata.objects.all()
    return render(request,template_name="IT/status.html",context={"t":t})