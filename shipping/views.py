
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
    return render(request,"shipping/shipment_upload.html",{"form":form})

def shipment_list(request):
    shipments=Shipment.objects.all()
    return render(request,"shipping/shipment_list.html",{"shipments":shipments})

def shipment_detail(request,id):
    shipment=Shipment.objects.get(id=id)
    return render (request,"shipping/shipment_details.html",{"shipment":shipment})

def shipment_edit(request,id):
    shipment=Shipment.objects.get(id=id)
    if request.method == "POST":
        form=ShipmentUploadForm(request.POST,instance=shipment)
        if form.is_valid():
            form.save()
        return redirect('shipment_details',id=id)
    return render(request,"shipping/edit_shipment.html",{'form':form})





