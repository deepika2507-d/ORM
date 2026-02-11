# Ex01 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
admin.py

from django.contrib import admin
from .models import Employee,EmployeeAdmin
admin.site.register(Employee,EmployeeAdmin)

models.py

from django.db import models
from django.contrib import admin
class Employee(models.Model):
    OrderID = models.IntegerField(primary_key=True)
    UserID = models.CharField(max_length=100)
    OrderDate = models.DateField()
    ItemName = models.CharField()
    OrderQty =models.IntegerField()
    UnitPrice = models.FloatField()
    TotalAmount = models.FloatField()
    DeliveryAddress = models.CharField()

class EmployeeAdmin(admin.ModelAdmin): 
        list_display=( 'OrderID','UserID','OrderDate','ItemName','OrderQty','UnitPrice','TotalAmount','DeliveryAddress')
## OUTPUT

Include the screenshot of your admin page.


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
