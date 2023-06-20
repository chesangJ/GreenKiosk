from django.contrib import admin

# Register your models here.
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    payment_details=Payment("amount","date_of_payment","pending_payment","payment_methods","date_created","date_updated")

admin.site.register(Payment,PaymentAdmin)   