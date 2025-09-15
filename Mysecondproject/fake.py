import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mysecondproject.settings')


import django
django.setup()

from faker import Faker

from random import randint

from CRUDapp.models import Employeedetails



fake=Faker()



def Fakedatas():
    Employeename=fake.name()
    Employeeid=randint(1,999)
    Employeecity=fake.city()
    Employeedetails.objects.get_or_create(Empname=Employeename,Empid=Employeeid,Empcity=Employeecity)

for _ in range(1,10,1):
        Fakedatas()



