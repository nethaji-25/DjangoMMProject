from django.urls import path
from Modelapp import views

urlpatterns=[
    path('empdetail/',views.Details,name='empdetail'),
    path('reg/',views.Register,name='reg'),
    path('form/',views.Test)
]