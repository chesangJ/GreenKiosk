from django.contrib import admin

from shipping.models import Shipment

# Register your models here.
class ShipmentAdmin(admin.ModelAdmin):
    list_display= ("Location","Date_shipment_placed","Date_shipment_recieved","Product","Delivery_person","date_created","date_updated")

admin.site.register(Shipment,ShipmentAdmin)   