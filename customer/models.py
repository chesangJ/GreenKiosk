from django.db import models

# Create your models here.
class Customer(models.Model): 
    name = models.CharField(max_length=32)
    email=models.CharField(max_length=8)
    phonenumber=models.CharField(max_length=10)
    location=models.CharField(max_length=20)
   
    password=models.CharField(max_length=8)
    
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    



   
