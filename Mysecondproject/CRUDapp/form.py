from django import forms
from .models import Employeedetails

class Employeeform(forms.ModelForm):
    class Meta:
        model=Employeedetails
        fields="__all__"