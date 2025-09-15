from django.db import models

# Create your models here.

class Empdata(models.Model):
    Empid=models.IntegerField()
    Name=models.CharField(max_length=64)
    Designation=models.CharField(max_length=64)
    City=models.CharField(max_length=64)

    def __str__(self):
        return self.Name