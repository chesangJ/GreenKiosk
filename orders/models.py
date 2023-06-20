from django.db import models

# Create your models here.
class Orders(models.Model):
    date_time=models.DateTimeField()
    status=models.CharField(max_length=8)
    number_of_orders=models.IntegerField()
    total_amount=models.IntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
