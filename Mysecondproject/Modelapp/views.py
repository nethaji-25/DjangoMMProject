from django.shortcuts import render, HttpResponse, redirect

from .forms import RegisterForm, Testform
from .models import Employee


# Create your views here.

def Details(request):
    a=Employee.objects.all()

    return render(request,template_name="model/Employeedetails.html",context={"a":a})


def Register(request):
    if request.method=="POST":
        r=RegisterForm(request.POST)
        if r.is_valid():
            r.save()
            return redirect('empdetail')
    e=RegisterForm()
    return render(request,template_name="model/Register.html",context={"e":e})

def Test(request):
    t=Testform()
    return render(request,template_name="model/Form.html",context={"t":t})