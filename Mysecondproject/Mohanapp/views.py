from django.shortcuts import render
from .models import CRMPortal
from .form import Createform
from django.contrib import messages
# Create your views here.

def Dashboard(request):
    return render(request,template_name="MM/MMDash.html")

def Customer_details(request):
    c=CRMPortal.objects.all()

    return render(request,template_name="MM/Details.html",context={"c":c})

def Contact(request):
    return render(request,template_name="MM/Help.html")

def Createleads(request):
    if request.method=="POST":
        e=Createform(request.POST)
        if e.is_valid():
            e.save()
            messages.success(request,"A lead has been created successfully")
        else:
            messages.error(request,"Please fill all the fields")
    f=Createform()
    return render(request,template_name="MM/Create.html",context={"f":f})