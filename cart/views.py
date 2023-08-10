from django.shortcuts import redirect, render
from .form import CartUploadForm
from .models import Cart

def cart_upload_form(request):
    if request.method == 'POST':
        form=CartUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=CartUploadForm()
    return render(request,"cart/cart_upload.html",{"form":form})
    
def cart_list(request):  
     carts=Cart.objects.all()
     return render(request,"cart/cart_list.html",{"carts":carts})

def cart_detail(request,id):
     cart=Cart.objects.get(id=id)
     return render(request,"cart/cart_detail.html",{"cart":cart})

def cart_edit(request,id):
     cart=Cart.objects.get(id=id)
     if request.method=="POST":
          form=CartUploadForm(request.POST,instance=cart)
          if form.is_valid():
               form.save()
          return redirect('cart_detail_view',id=id)
     else:
          form=CartUploadForm(instance=cart)
          return render(request,'cart/edit_cart.html',{'form':form})






