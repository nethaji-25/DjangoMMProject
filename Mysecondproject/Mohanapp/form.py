from django import forms
from .models import CRMPortal

class Createform(forms.ModelForm):
    class Meta:
        model= CRMPortal
        fields="__all__"