from django.urls import path
from .views import vendor_upload_form,vendor_list,vendor_details,vendor_edit

urlpatterns=[
    path('vendor/upload',vendor_upload_form,name='vendor_upload_view'),
    path('vendor/list/',vendor_list,name='vendor_list_view'),
    path('vendor/<int:id>/',vendor_details,name='vendor_details_view'),
    path('vendor/<int:id>/edit',vendor_edit,name='vendor_edit_view')
    
]