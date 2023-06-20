from django.contrib import admin

# Register your models here.
from .models import Notification
class NotificationAdmin(admin.ModelAdmin):
    notification_details=Notification("Sende_Name","title","description","message","date_time","date_created","date_updated")

admin.site.register(Notification,NotificationAdmin)   