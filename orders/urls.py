from .views import order_upload,order_list,order_detail,edit_order
from django.urls import path


urlpatterns=[
    path('orders/upload',order_upload,name='order_upload_view'),
    path('orders/list/',order_list,name='order_list_view'),
    path('orders/<int:id>/',order_detail,name='order_details_view'),
    path('orders/<int:id>/edit',edit_order,name='edit_order_view')
]