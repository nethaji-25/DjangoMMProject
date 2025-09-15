from rest_framework import serializers
from .models import Empdata

class Userserialize(serializers.ModelSerializer):
    class Meta:
        model=Empdata
        fields="__all__"