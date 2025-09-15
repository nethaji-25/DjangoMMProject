from django.urls import path
from Restapp import views

urlpatterns=[
    path('getapi/',views.get_api,name='getapi'),
    path('postapi/',views.post_api,name='postapi'),
    path('putapi/<id>',views.put_api,name='putapi'),
    path('deleteapi/<id>',views.delete_api,name='deleteapi')
]