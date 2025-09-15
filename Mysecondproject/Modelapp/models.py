from django.db import models

# Create your models here.

class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=64)
    eage=models.IntegerField()

    def __str__(self):
        return self.ename


