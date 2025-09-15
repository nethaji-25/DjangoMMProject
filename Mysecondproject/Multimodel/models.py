
from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Employee(models.Model):
    ename=models.CharField(max_length=64)
    eage=models.IntegerField()
    enumber=models.IntegerField()
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename
