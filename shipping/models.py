from django.db import models
from orders.models import Orders
# Create your models here.
class Shipment(models.Model): 
    Location = models.CharField(max_length=32)
    Date_shipment_placed=models.DateTimeField()
    Date_shipment_recieved=models.DateTimeField()
    Product=models.CharField(max_length=20)
    Delivery_person=models.CharField(max_length=20)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    orders=models.ManyToManyField(Orders)

    def __str__(self):
        return self.Location