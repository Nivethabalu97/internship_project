from django.urls import path

from myaccount import views
urlpatterns = [

    path('',views.register,name='register'),
    path('getregister',views.getregister,name='getregister'),
    path('login',views.login,name='login'),
    path('logout/',views.logout,name='logout'),


    ]

