from django.urls import path
from Secondapp import views
urlpatterns=[
    path('empdetails/',views.Empdetails)
]