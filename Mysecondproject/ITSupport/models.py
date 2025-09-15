from django.db import models




# Create your models here.

class Ticketsdata(models.Model):
    STATUS_CHOICES = [
        ("open", "Open"),
        ("in_progress", "In Progress"),
        ("closed", "Closed"),
    ]
    PRIORITY_CHOICES = [
        ("Priority 1", "Top Priority"),
        ("Priority 2", "Priority"),
        ("Priority 3", "Low"),
    ]

    Employeename=models.CharField(max_length=64)
    Summary=models.CharField(max_length=64)
    Description=models.CharField(max_length=100)
    Priority=models.CharField(choices=PRIORITY_CHOICES,default="Priority 3")
    Status=models.CharField(max_length=64,choices=STATUS_CHOICES,default="open",null=False)
    def __str__(self):
        return self.Employeename


