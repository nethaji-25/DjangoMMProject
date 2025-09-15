from django.urls import path
from ITSupport import views

urlpatterns=[
    path('raiseticket/',views.Submitticket,name='raiseticket'),
    path('dash/',views.Dashboard,name='dash'),
    path('contact/',views.Contact,name='contact'),
    path('get_detail/',views.Gettickets,name='get_detail'),
    path('status/',views.Ticketstatus,name='status')
]