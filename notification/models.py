from django.db import models

# Create your models here.
class Notification(models.Model):
    Recievers_Name=models.CharField(max_length=50)
    title=models.CharField(max_length=8)
    description=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    date_time=models.DateTimeField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Recievers_Name
