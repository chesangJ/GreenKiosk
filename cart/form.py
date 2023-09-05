from django import forms
from .models import Cart

class CartUploadForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields="__all__"
        unique_together = (('customer',),)
       


     
