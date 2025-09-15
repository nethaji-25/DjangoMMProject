from django.urls import path
from CRUDapp import views


urlpatterns=[
    path('get/',views.Getemployees,name='get'),
    path('register/',views.Addemployees,name='register'),
    path('delete/<id>',views.Deleteemployee,name='delete'),
    path('update/<id>',views.Updateemployee,name='update'),
    path('search/',views.Searchemployee,name='search'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout')
]