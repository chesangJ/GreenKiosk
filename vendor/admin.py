from django.contrib import admin

# Register your models here.
from .models import Vendor
class VendorAdmin(admin.ModelAdmin):
    vendor_details=Vendor("name","email","phonenumber","location","password","date_created","date_updated")

admin.site.register(Vendor,VendorAdmin)   