from django import forms

from .models import Product

class ProductUploadForms(forms.ModelForm):
    # model you want to create a form for
    class Meta:
        model=Product
        fields="__all__"