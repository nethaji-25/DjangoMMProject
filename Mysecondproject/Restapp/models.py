from django.db import models

# Create your models here.

class Employeedetails(models.Model):
    employee_name=models.CharField(max_length=64)
    employee_id=models.IntegerField()
    employee_designation=models.CharField(max_length=64)

    def __str__(self):
        return self.employee_name
