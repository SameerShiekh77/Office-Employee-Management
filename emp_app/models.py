
from django.db import models
from django.utils import timezone
# Create your models here.

class Department(models.Model):

    name = models.CharField(max_length=50, null=False)    
    location = models.CharField(max_length=50,default="Aptech North Karachi")    


    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name

class Employee(models.Model):
    class EmployeeObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset()
    
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    depart = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary= models.IntegerField()
    bonus= models.IntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone= models.IntegerField()
    hireDate = models.DateTimeField(default=timezone.now)
    objects = models.Manager()  # default manager
    employeeobjects = EmployeeObjects()  # custom manager

    
    
    def __str__(self):

