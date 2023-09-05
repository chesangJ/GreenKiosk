from django.urls import path
from .views import notification_upload_form,notification_list,notification_details

urlpatterns=[
    path("notification/list",notification_list,name="notification_list_view"),
    path("notification/<int:id>",notification_details,name="notification_details_view"),
    path("notification/upload",notification_upload_form,name="notification_upload_view"),
    
]