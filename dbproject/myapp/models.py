from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30,null=True)
    age = models.IntegerField(null=True)
    marks = models.IntegerField(null=True)
    stype = models.BooleanField(default=False)

class Employee(models.Model):
    name = models.CharField(max_length=25,null=True)
    age = models.IntegerField(null=True)
    position = models.CharField(max_length=50)
    years = models.IntegerField(default=True)


class Emp(models.Model):
    name = models.CharField(max_length=25, null=True)
    age = models.IntegerField(null=True)
    position = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    emp_roll = models.IntegerField(null=True)
