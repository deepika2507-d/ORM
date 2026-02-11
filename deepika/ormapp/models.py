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