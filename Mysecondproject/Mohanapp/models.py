from django.db import models

# Create your models here.

LEAD_STATUS = [
    ("new", "New"),
    ("contacted", "Contacted"),
    ("qualified", "Qualified"),
    ("converted", "Converted"),
    ("lost", "Lost"),
]

SOURCE_CHOICES = [
    ("web", "Website"),
    ("email", "Email"),
    ("phone", "Phone"),
    ("referral", "Referral"),
    ("ads", "Ads"),
    ("other", "Other"),
]

class CRMPortal(models.Model):
    Customername=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    Company=models.CharField(max_length=200)
    Contactnumber=models.IntegerField()
    Status=models.CharField(max_length=20,choices=LEAD_STATUS)
    Sources=models.CharField(max_length=20,choices=SOURCE_CHOICES)

    def __str__(self):
        return self.Customername


