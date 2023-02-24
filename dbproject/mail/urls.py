from django.urls import path

from mail import views
urlpatterns = [

    path('',views.viewmail,name='mail'),
    path('viewmail',views.mymail,name='viewmail'),
    ]