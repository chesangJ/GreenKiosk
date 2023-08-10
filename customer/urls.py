from .views import customer_upload_form,customer_list,customer_detail,customer_edit
from django.urls import path


urlpatterns=[
    path('customer/upload',customer_upload_form,name='customer_upload_view'),
    path('customer/list',customer_list,name='customer_list_view'),
    path('customer/<int:id>/',customer_detail,name='customer_detail_view'),
    path('customer/<int:id>/edit',customer_edit,name='edit_customer_view')
]
#    path("product/<int:id>/",product_details,name='product_details_view'),
# path("product/<int:id>/",edit_product_view,name='edit_product_view')