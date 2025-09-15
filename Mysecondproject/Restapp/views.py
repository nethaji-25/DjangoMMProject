from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



from .models import Employeedetails
from .Userserializer import Createserializer

# Create your views here.

@api_view(['GET'])
def get_api(request):
    e=Employeedetails.objects.all()
    c=Createserializer(e,many=True)
    return Response(c.data)

@api_view(['POST'])
def post_api(request):
    c=Createserializer(data=request.data)
    if c.is_valid():
        c.save()
        return Response(c.data,status=status.HTTP_201_CREATED)
    else:
        return Response(c.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_api(request,id):
    e=Employeedetails.objects.get(id=id)
    c=Createserializer(e,data=request.data)
    if c.is_valid():
        c.save()
        return Response(c.data)

@api_view(['DELETE'])
def delete_api(request,id):
    e=Employeedetails.objects.get(id=id)
    e.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
