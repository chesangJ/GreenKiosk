# construct urls
from django.urls import path

# create the path to the view we have created upload product 
from .views import upload_product,product_list,product_details,add_to_cart
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        



urlpatterns=[
    path("product/upload",upload_product,name="product-upload-view"),
    path("product/list",product_list,name='product_list_view'),
    path("product/<int:id>/",product_details,name='product_details_view'),
   path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),

    ]