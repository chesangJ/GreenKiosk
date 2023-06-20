from django.contrib import admin

# Register your models here.
from .models import Orders
class OrdersAdmin(admin.ModelAdmin):
    orders_details=Orders("date_time","status","number_of_orders","total_amount","date_created","date_updated")

admin.site.register(Orders,OrdersAdmin)   