from django.urls import path
from .views import CustomerListView, ProductListView,CartListView,OrderListView

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer_list_view'),
    path('products/', ProductListView.as_view(), name='product_list_view'),
    path('cart/', CartListView.as_view(), name='cart_list_view'),
    path('order/', OrderListView.as_view(), name='order_list_view'),
    
    

]
