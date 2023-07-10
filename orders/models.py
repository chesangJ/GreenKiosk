
from django.db import models

from payment.models import Payment
from customer.models import Customer
from cart.models import Cart
class Orders(models.Model):
    date_time=models.DateTimeField()
    status=models.CharField(max_length=8)
    number_of_orders=models.IntegerField()
    total_amount=models.IntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    payment=models.OneToOneField(Payment,on_delete=models.CASCADE,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.customer.name
