from django import forms
from .models import Employee

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"


class Testform(forms.Form):
    Name=forms.CharField(min_length=3,max_length=64)
    Age=forms.IntegerField(min_value=3,max_value=25)
    Email=forms.EmailField()
    Image=forms.ImageField()
    Files=forms.FileField()
    WriteText=forms.CharField(max_length=64,widget=forms.TextInput())
    Selectfromlist=forms.ChoiceField(choices=[('a','Apple'),('o','Orange'),('m','Mango')])
    Selectfromlist=forms.MultipleChoiceField(choices=[('a','Apple'),('o','Orange'),('m','Mango')])
    active=forms.BooleanField()
    Option=forms.ChoiceField(choices=[('m','Male'),('f','Female')],widget=forms.RadioSelect())
    DecimalValue=forms.DecimalField(max_digits=2,decimal_places=2)