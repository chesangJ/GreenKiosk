from django.db import models
from django.contrib.auth.models import User
from inventory.models  import Product
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=10, decimal_places=2 )
    quantity=models.PositiveIntegerField()
    image=models.ImageField()
    products=models.ManyToManyField(Product)
    def __str__(self):
        return self.product

