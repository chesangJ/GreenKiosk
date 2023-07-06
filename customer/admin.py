from django.contrib import admin

# Register your models here.
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display= ("name","email","phonenumber","location","password","date_created","date_updated")

admin.site.register(Customer,CustomerAdmin)   

