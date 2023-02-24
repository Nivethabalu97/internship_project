from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('student/',views.studetails,name='studetails'),
    path('addstudentdetails',views.addstudentdetails,name='addstudentdetails'),
    path('employee/',views.empdetails,name='empdetails'),
    path('addempdetails',views.addempdetails,name='addempdetails'),
    path('test/',views.test,name='test'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('addemp/',views.addemp,name='addemp'),
    path('emdetails',views.addem,name='addem'),
    path('viewdetails/',views.viewem,name='viewem'),
    path('delemp<int:id>',views.delemp,name='delemp'),
    path('filterdetails/',views.filterdetails,name='filterdetails'),
    path('filterfun',views.filterfun,name='filterfun'),
    path('getForm/',views.getForm,name='getForm'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),


]
