from django.urls import path
from Testapp import views


urlpatterns=[
    path('get/',views.Getdata,name='get'),
    path('post/',views.postdata,name='post'),
    path('delete/<id>',views.deletedata,name='delete'),
    path('put/<id>',views.putdata,name='put'),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logout_page,name='logout'),
    path('register/',views.Registeruser,name='register'),
    path('search/',views.Searchemployee,name='search'),
    path('getapi/',views.get_api,name='getapi'),
    path('postapi/',views.post_api,name='postapi'),
    path('putapi/<id>',views.put_api,name='putapi'),
    path('deleteapi/<id>',views.delete_api,name='deleteapi')
]