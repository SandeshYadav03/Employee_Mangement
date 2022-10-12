from django.db import models


class Employee(models.Model):
    firstname = models.CharField(max_length=100, null=False)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    mobile = models.IntegerField(default=0)
    alt_no = models.IntegerField(default=0)
    email = models.CharField(max_length=100)
    blood = models.CharField(max_length=100)
    
    def __str__(self):
       return self.firstname
   
