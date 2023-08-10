from django.shortcuts import redirect, render
from .form import VendorUploadForm
from .models import Vendor

def vendor_upload_form(request):
    if request.method =='POST':
        form =VendorUploadForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('vendor_list_view')
    else:
        form=VendorUploadForm()
    return render (request,'vendor/vendor_upload.html',{'form':form})

def vendor_list(request):
    vendors=Vendor.objects.all()
    return render(request,'vendor/vendor_list.html',{'vendors':vendors})

def vendor_details(request,id):
    vendor=Vendor.objects.get(id=id)
    return render(request,'vendor/vendor_details.html',{'vendor':vendor})

def vendor_edit(request,id):
    vendor=Vendor.objects.get(id=id)
    if request.method == 'POST':
        form=VendorUploadForm(request.POST,instance=vendor)
        if form.is_valid():
         form.save()
        return redirect('vendor_details_view',id=id)
    else:
        form=VendorUploadForm(instance=vendor)
        return render(request,'vendor/edit_vendor.html',{'form':form})