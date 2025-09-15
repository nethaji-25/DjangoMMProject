from django.db import models

# Create your models here.

class Employeedetails(models.Model):
    Empname=models.CharField(max_length=64)
    Empid=models.IntegerField()
    Empcity=models.CharField(max_length=64)

    def __str__(self):
        return self.Empname

