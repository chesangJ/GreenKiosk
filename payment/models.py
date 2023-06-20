from django.db import models

# Create your models here.
class Payment(models.Model):
    amount=models.IntegerField()
    date_of_payment=models.DateTimeField()
    pending_payment=models.BooleanField()
    payment_method=models.CharField(max_length=8)
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
