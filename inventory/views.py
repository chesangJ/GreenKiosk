from django.shortcuts import render
from django.shortcuts import redirect
from inventory.models import Product
from .form import ProductUploadForms

# Create your views here.
# processes an http request
# handles an hhtp request

def upload_product(request):
    #post being able to save the data
    if request.method =="POST": 
      uploaded_product = request.FILES["image"]
      form=ProductUploadForms(request.POST,request.FILES)
      if form.is_valid():
       form.save()
    else: 
       form=ProductUploadForms()
    return render(request,'inventory/product-upload.html',{"form":form})

def product_list(request):
   products=Product.objects.all()
   return render(request,'inventory/product_list.html',{'products':products})

def product_details(request,id):
   product=Product.objects.get(id=id)
   return render(request,'inventory/product_details.html',{'product':product})
def addToCart (request):
   cartItems=[]
   return render(request,'inventory/cart.html',{'cartItems':cartItems})
def edit_product_view(request,id):
   product=Product.objects.get(id=id)
   if request.method=="POST":
    form=ProductUploadForms(request.POST,instance=product)
   if form.is_valid():
      form.save()
      return redirect('product_details',id=id)
   else:
      form=ProductUploadForms(instance=product)
      return render(request,'inventory/edit.html',{'form':form})
   



   