from django.shortcuts import render

from django.shortcuts import redirect
from .form import OrderUploadForm
from .models import Orders
 
def order_upload(request):
    if request.method=='POST':
        form=OrderUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=OrderUploadForm()
    return render(request,"orders/order_upload.html",{"form":form})

def order_list(request):
    orders=Orders.objects.all()
    return render(request,"orders/order_list.html",{"orders":orders})

def order_detail(request,id):
    order=Orders.objects.get(id=id)
    return render(request,"orders/order_details.html",{'order':order})

def edit_order(request,id):
    order=Orders.objects.get(id=id)
    if request.method=='POST':
        form=OrderUploadForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
        return redirect('order_detail',id=id)
    else:
        form=OrderUploadForm(instance=order)
        return render(request,'orders/edit_order.html',{'order':order})





