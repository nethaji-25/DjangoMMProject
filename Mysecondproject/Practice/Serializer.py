from rest_framework import serializers
from .models import Myemployeedetails


class Serializeemp(serializers.ModelSerializer):
    class Meta:
        model=Myemployeedetails
        fields="__all__"