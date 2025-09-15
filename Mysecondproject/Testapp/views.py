from django.shortcuts import render, redirect
from .models import Empdata
from .form import Userform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import Registerform
from django.db.models import Q
from rest_framework.decorators import api_view
from .Serialize import Userserialize
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@login_required(login_url='login')
def Getdata(request):
    e=Empdata.objects.all()
    return render(request,template_name='Test/Get.html',context={"e":e})

def postdata(request):
    if request.method=="POST":
        data=Userform(request.POST)
        if data.is_valid():
            data.save()
            return redirect('get')
    u=Userform()
    return render(request,template_name="Test/form.html",context={"u":u})

def deletedata(request,id):
    e=Empdata.objects.get(id=id)
    e.delete()
    return redirect('get')

def putdata(request,id):
    e=Empdata.objects.get(id=id)
    if request.method=="POST":
        u=Userform(request.POST,instance=e)
        if u.is_valid():
            u.save()
            return redirect('get')
    return render(request,template_name="Test/Update.html",context={"e":e})

def loginpage(request):
    if request.method=="POST":
        a=request.POST.get("userid")
        b=request.POST.get("password")
        n=authenticate(request,username=a,password=b)
        if n is not None:
            login(request,n)
            return redirect('get')

        else:
            messages.error(request,"Incorrect Username or Password")

    return render(request,template_name="Test/Loginpage.html")

def logout_page(request):
    logout(request)
    return redirect('login')

def Registeruser(request):
    if request.method=="POST":
        a=Registerform(request.POST)
        if a.is_valid():
            a.save()
            return redirect('login')
        else:
            messages.error(request,"Enter valid details")

    r=Registerform()

    return render(request,template_name="Test/Register.html",context={"r":r})


def Searchemployee(request):
    r=request.GET.get("find")
    if r:
        e=Empdata.objects.filter(Q(Empid__icontains=r) | Q(Name__icontains=r) | Q(Designation__icontains=r) | Q(City__icontains=r))
    else:
        e=Empdata.objects.all()
    return render(request,template_name="Test/Get.html",context={"e":e})

@api_view(['GET'])
def get_api(request):
    e=Empdata.objects.all()
    s=Userserialize(e,many=True)
    return Response(s.data)
@api_view(['POST'])
def post_api(request):
    s=Userserialize(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data,status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_api(request,id):
    e=Empdata.objects.get(id=id)
    s=Userserialize(e,data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_api(request,id):
    e=Empdata.objects.get(id=id)
    e.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
