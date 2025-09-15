from django import forms
from .models import Ticketsdata

class Userform(forms.ModelForm):
    class Meta:
        model= Ticketsdata
        fields="__all__"
        exclude=['Status']
        widgets = {
            'Employeename': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name',
                'autocomplete':'off',


            }),
            'Summary': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'One-line summary',
                'autocomplete': 'off',


            }),
            'Description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe the issue',
                'autocomplete': 'off',


            }),

            'Priority': forms.Select(attrs={
                'class': 'form-select',
                'autocomplete': 'off'

            }),
        }