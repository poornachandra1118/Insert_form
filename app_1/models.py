from django.db import models

# Create your models here.

class Employee(models.Model):
    Emp_id=models.CharField(max_length=50,null=False,blank=False)
    Emp_name=models.CharField(max_length=100,null=False,blank=True)
    Emp_mobile=models.CharField(max_length=10,null=False,blank=True)
    Emp_email=models.EmailField(max_length=150)
    Emp_status=models.BooleanField(default=True)
    