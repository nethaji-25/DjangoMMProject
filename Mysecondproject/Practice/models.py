from django.db import models

# Create your models here.

class Myemployeedetails(models.Model):
    employeeid=models.IntegerField()
    employeename=models.CharField(max_length=64)
    employeecity=models.CharField(max_length=64)

    def __str__(self):
        return self.employeename