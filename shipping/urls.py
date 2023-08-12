from django.urls import path
from .views import shipment_upload_form,shipment_list,shipment_detail,shipment_edit

urlpatterns=[
    path('shipping/upload/',shipment_upload_form,name='shipment_upload_view'),
    path('shipping/<int:id>/',shipment_detail,name='shipment_detail_view'),
    path('shipping/list/',shipment_list,name='shipment_list_view'),
    path('shipping/<int:id>/',shipment_edit,name='edit_shipment_view')
]