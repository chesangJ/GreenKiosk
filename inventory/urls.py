# construct urls
from django.urls import path

# create the path to the view we have created upload product 
from .views import upload_product,product_list,product_details,addToCart,edit_product_view
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        



urlpatterns=[
    path("product/upload",upload_product,name="product-upload-view"),
    path("product/list",product_list,name='product_list_view'),
    path("product/<int:id>/",product_details,name='product_details_view'),
    path("addToCart/",addToCart,name='addToCart_view'),
    path("product/<int:id>/",edit_product_view,name='edit_product_view')
    ]