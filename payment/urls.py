from .views import payment_upload_form,payment_detail,payment_list,payment_edit
from django.urls import path


urlpatterns=[
    path('payment/upload',payment_upload_form,name='payment_upload_view'),
    path('payment/list/',payment_list,name='payment_list_view'),
    path('payment/<int:id>/',payment_detail,name='payment_details_view'),
    path('payment/<int:id>/edit',payment_edit,name='edit_payment_view')
]