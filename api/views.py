from rest_framework.views import APIView
from customer.models import Customer
from .serializers import CustomerSerializer
from rest_framework.response  import Response
from rest_framework import status

class CustomerListView(APIView):
    def get(self,request):
         customer=Customer.objects.all()
         serializer =CustomerSerializer(customer,many=True)
         
         return Response(serializer.data)
    
    # def post(self,request):
    #      serializer=CustomerSerializers(data= request.data)

    #      if serializer.is_valid():
    #         serializer.save()
    #      return Response




        


          
     


       