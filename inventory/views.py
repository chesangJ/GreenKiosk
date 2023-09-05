from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from inventory.models import Product
from .form import ProductUploadForms
from cart.models import Cart

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
   
    query = request.GET.get('q')  # Get the search query from the URL parameter
    
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
   

    return render(request,'inventory/product_list.html',{'products':products})

def product_details(request,id):
   product=Product.objects.get(id=id)
   return render(request,'inventory/product_details.html',{'product':product})

def add_to_cart(request, id):
    product = get_object_or_404(Product, pk=id)
    
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product.name,
        defaults={'price': product.price, 'quantity': 1, 'image': product.image}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_detail')
   



   