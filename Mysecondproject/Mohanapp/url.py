from django.urls import path
from Mohanapp import views

urlpatterns=[
    path('dash/',views.Dashboard,name='dash'),
    path('get/',views.Customer_details,name='get'),
    path('help/',views.Contact,name='help'),
    path('create/',views.Createleads,name='create')
]