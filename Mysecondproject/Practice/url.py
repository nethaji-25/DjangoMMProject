from django.urls import path
from Practice import views

urlpatterns=[
    path('getapi/',views.get_api,name='getapi'),
    path('postapi/',views.post_api,name='postapi'),
    path('putapi/<id>',views.put_api,name='putapi'),
    path('delapi/<id>',views.delete_api,name='delapi')
]