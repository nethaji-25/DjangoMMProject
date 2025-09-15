from django.urls import path
from Alertapp import views

urlpatterns=[
    path("alert/",views.Test,name='alert')
]