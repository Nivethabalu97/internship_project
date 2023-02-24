from django.contrib import admin

# Register your models here.
from myapp.models import Employee, Student,Emp

admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Emp)