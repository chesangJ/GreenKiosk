from django.shortcuts import redirect, render
from .form import CustomerUploadForm
from .models import Customer
 
def customer_upload_form(request):
    if request.method =='POST':
        form=CustomerUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerUploadForm()
    return render(request,"customer/customer_upload.html",{"form":form})

def customer_list(request):
    customers=Customer.objects.all()
    return render(request,"customer/customer_list.html",{"customers":customers})

def customer_detail(request,id):
    customer=Customer.objects.get(id=id)
    return render(request,"customer/customer_detail.html",{"customer":customer})

def customer_edit(request,id):
    customer=Customer.objects.get(id=id)
    if request.method == "POST":
        form=CustomerUploadForm(request.POST,instance=customer)
        if form.is_valid():
           form.save
        return redirect('customer_detail_view',id=id)
    else:
        form=CustomerUploadForm(instance=customer)
        return render(request,'customer/edit_customer.html',{'form':form})
    

