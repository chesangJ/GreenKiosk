
from django.shortcuts import redirect, render
from .form import PaymentUploadForm
from .models import Payment
 
def payment_upload_form(request):
    if request.method =='POST':
        form=PaymentUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=PaymentUploadForm()
    return render(request,"payment/payment_upload.html",{"form":form})

def payment_list(request):
    payments=Payment.objects.all()
    return render(request,"payment/payment_list.html",{"payments":payments})

def payment_detail(request,id):
    payment=Payment.objects.get(id=id)
    return render(request,"payment/payment_details.html",{"payment":payment})

def payment_edit(request,id):
    payment=Payment.objects.get(id=id)
    if request.method == "POST":
        form=PaymentUploadForm(request.POST,instance=payment)
        if form.is_valid():
           form.save
        return redirect('payment_detail',id=id)
    else:
        form=PaymentUploadForm(instance=payment)
        return render(request,'payment/edit_payment.html',{'form':form})
    


