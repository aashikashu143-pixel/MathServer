from django.db import models
from django.db import models
from django.contrib import admin
class ecom(models.Model):
    pro_ID=models.CharField(primary_key=True,max_length=7)
    pname=models.CharField(max_length=30)
    cost=models.CharField(max_length=10)
    brand=models.CharField(max_length=1)
    expdate=models.DateTimeField()
    helpcentre=models.EmailField()
    shipdate=models.DateTimeField()

class ecomAdmin(admin.ModelAdmin):
    list_display=["pro_ID","pname","cost","brand","expdate","helpcentre","shipdate"]