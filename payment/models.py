from django.db import models

from customer.models import Customer
# Create your models here.
class Payment(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount=models.IntegerField()
    date_of_payment=models.DateTimeField()
    pending_payment=models.BooleanField()
    payment_methods=models.CharField(max_length=8)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.customer.name
