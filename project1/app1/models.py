from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    roll_no=models.IntegerField()
    mail=models.EmailField()
    mobileno=models.IntegerField()
    address=models.CharField(max_length=100)
    dateofbirth=models.DateField()
    marks=models.FloatField()
