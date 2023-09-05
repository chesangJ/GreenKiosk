from django.urls import path
from  .views import cart_detail,add_to_cart,remove_from_cart,checkout

urlpatterns = [
    path('cart/',cart_detail, name='cart_detail'),
    path('add_to_cart/<int:product_id>/',add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/',checkout, name='checkout'),
    
]
