from django.db import models

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
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    depart = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary= models.IntegerField()
    bonus= models.IntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone= models.IntegerField()
    hireDate = models.DateField()

    def __str__(self):
        return self.first_name + " " +self.last_name