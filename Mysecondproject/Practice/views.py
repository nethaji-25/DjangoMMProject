from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Myemployeedetails
from .Serializer import Serializeemp
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated




# Create your views here.


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_api(request):
    m=Myemployeedetails.objects.all()
    s=Serializeemp(m,many=True)
    return Response(s.data)

@api_view(['POST'])
def post_api(request):
    s=Serializeemp(data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data,status=status.HTTP_201_CREATED)
    else:
        return Response(s.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_api(request,id):
    m=Myemployeedetails.objects.get(id=id)
    s=Serializeemp(m,data=request.data)
    if s.is_valid():
        s.save()
        return Response(s.data,status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_api(request,id):
    m=Myemployeedetails.objects.get(id=id)
    m.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)