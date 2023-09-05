from django.shortcuts import redirect, render
from .form import NotificationUploadForm
from .models import Notification

def notification_upload_form(request):
    if request.method =='POST':
        form=NotificationUploadForm(request.POST)
        if form.is_valid:
            form.save()
        else:
            form=NotificationUploadForm()
        return render(request,"notification/notification_upload.html",{"form":form})
    
def notification_list(request):
    notifications=Notification.objects.all()
    return render(request,"notification/notification_list.html",{"notifications":notifications})

def notification_details(request,id):
    notification=Notification.objects.get(id=id)
    return render(request,"notification/notification_details.html",{"notification":notification})


    




#


