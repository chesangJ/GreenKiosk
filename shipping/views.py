
from django.shortcuts import redirect, render
from .form import ShipmentUploadForm
from .models import Shipment

def shipment_upload_form(request):
    if request.method =='POST':
        form=ShipmentUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ShipmentUploadForm()
    return render(request,"shipment/shipment_upload.html",{"form":form})

def shipment_list(request):
    shipments=Shipment.objects.all()
    return render(request,"shipment/shipment_list.html",{"shipments":shipments})

def shipment_detail(request,id):
    shipment=Shipment.objects.get(id=id)
    return render (request,"shipment/shipment_details.html",{"shipment":shipment})

def shipment_edit(request,id):
    shipment=Shipment.objects.get(id=id)
    if request.method == "POST":
        form=ShipmentUploadForm(request.POST,instance=shipment)
        if form.is_valid():
            form.save()
        return redirect('shipment_details',id=id)
    return render(request,'shipment/edit_shipment.html',{'form':form})


#

# def customer_edit(request,id):
#     customer=Customer.objects.get(id=id)
#     if request.method == "POST":
#         form=CustomerUploadForm(request.POST,instance=customer)
#         if form.is_valid():
#            form.save
#         return redirect('customer_detail',id=id)
#     else:
#         form=CustomerUploadForm(instance=customer)
#         return render(request,'customer/edit_customer.html',{'form':form})
    



