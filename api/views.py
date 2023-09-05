from django.http import Http404
import orders
from orders.models import Orders
from rest_framework.views import APIView
from customer.models import Customer
from inventory.models import Product
from .serializers import CustomerSerializer
from .serializers import ProductSerializer
from cart .models import Cart
from .serializers import CartSerializer
from .serializers import OrderSerializer
from rest_framework.response  import Response
from rest_framework import status
from api import serializers

class CustomerListView(APIView):
    def get(self,request):
         customer=Customer.objects.all()
         serializer =CustomerSerializer(customer,many=True)
         return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomerDetailView(APIView):
    def get_object(self, id):
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, format=None):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   


class ProductListView(APIView):
    def get(self,request):
         product=Product.objects.all()
         serializer =ProductSerializer(product,many=True)
         return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductDetailView(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Product = self.get_object(pk)
        serializer = ProductSerializer(Product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product= self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   


   
class CartListView(APIView):
    def get(self,request):
         cart=Cart.objects.all()
         serializer =CartSerializer(cart,many=True)
         return Response(serializer.data)
    
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CartDetailView(APIView):
    def get_object(self, id):
        try:
            return Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Cart = self.get_object(pk)
        serializer = CartSerializer(Cart)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cart= self.get_object(pk)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart= self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderListView(APIView):
    def get(self,request):
         order=Orders.objects.all()
         serializer =OrderSerializer(order,many=True)
         return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderDetailView(APIView):
    def get_object(self, id):
        try:
            return orders.objects.get(id=id)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        order= self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart= self.get_object(pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   


      
   


          
     


       

          
     


       