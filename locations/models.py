from django.db import models

# Create your models here.

class Hospital(models.Model):
    name=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    number=models.CharField(max_length=50,null=True)
    time=models.CharField(max_length=50,null=True)
    longitude=models.DecimalField(max_digits=10, decimal_places=6)
    latitude=models.DecimalField(max_digits=10, decimal_places=6)

class Lesson(models.Model):
    name=models.CharField(max_length=50,null=True)
    address=models.CharField(max_length=50,null=True)
    number=models.CharField(max_length=50,null=True)
    time=models.CharField(max_length=50,null=True)
    longitude=models.DecimalField(max_digits=10, decimal_places=6)
    latitude=models.DecimalField(max_digits=10, decimal_places=6)



    
