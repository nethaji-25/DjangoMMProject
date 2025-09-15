from django.shortcuts import render

# Create your views here.


def Empdetails(request):
    return render(request,template_name="first/Details.html")
